.. _How-Jep-Works:

How *jtypes.jep* Works
**********************

Basics
======

*jtypes.jep* uses JNI and the CPython API to start up the Python interpreter inside
the JVM. The initial main interpreter will never be used except to initialize
and shut down Python. When you create a Jep instance in Java, a sub-interpreter
will be created for that Jep instance and will remain in memory until the Jep instance
is closed with jep.close(). The initial main interpreter will remain in the JVM
until the JVM exits.

Sandboxed interpreters
======================

Each Jep instance's sub-interpreter is sandboxed apart from the other sub-interpreters
to some degree. This means a change to the global variables in one interpreter will not
be reflected in other sub-interpreters. However, this rule does not apply to CPython
extensions.  There is no way to strictly enforce a CPython extension is implemented
in a way that supports sandboxing.
A simple example would be if a CPython extension library has a global static variable
that is used throughout the library. A change to that static variable in one
sub-interpreter would affect the other sub-interpreters since it is the same reference
in memory.  Note that the same rule applies to Java static variables or singletons.
Since only one exists in the JVM, a change to that static variable will be reflected
in all Python sub-interpreters.

*jtypes.jep* introduced the concept of shared modules.
Shared modules intentionally step outside of the sandboxed sub-interpreters to share
a module across sub-interpreters.  This can be used to workaround issues with CPython
extensions.  It can also potentially be used to share Python modules and their state
with other sub-interpreters.

*jtypes.jep* introduced the concept of shared interpreters.
Shared interpreters share all modules while retaining their own globals dictionary.
This is an alternative way to workaround issues with CPython extentions.
All SharedInterpreter instances are shared with one another but remain separate from
*jtypes.jep* instances.

Threading complications
=======================

Due to the need to manage a consistent Python thread state, a thread that creates a Jep
instance must be reused for all method calls to that Jep instance. *jtypes.jep* will
enforce this and throw exceptions mentioning invalid thread access.

Objects
=======

*jtypes.jep* will automatically convert Java primitives, Strings, and jep.NDArrays
sent into the Python interpreter into Python primitives, strings, and numpy.ndarrays
respectively. The Python versions of these objects will have no reference to their
original Java counterparts, they are entirely new objects that exist solely in Python's
system memory.

A Java object that does not match one of the types listed above will automatically
be wrapped as a PyJObject (or one of its related classes).
A PyJObject wraps the reference to the original Java object and presents the Python
interpreter with an interface for understanding the object as a Python object.
From the point-of-view of the Python interpreter, a PyJObject is just another
Python object with a select set of attributes (fields and methods) on it.

Python strings, primitives, and numpy.ndarrays will be automatically converted to
their Java equivalent when passed/returned to Java.
These Java objects will be equivalent copies, not references to the Python objects.
``Jep.getValue(String)`` has support for some automatic conversions where
Python object -> Java object:

* None -> null
* PyJClass (wrapped class) -> java.lang.Class
* PyJObject (wrapped object) -> java.lang.Object
* Python 2 Str -> java.lang.String
* Python 3 Str -> java.lang.String
* Python 3 Unicode -> java.lang.String
* True -> java.lang.Boolean
* False -> java.lang.Boolean
* Python 2 Int -> java.lang.Integer
* Python 2 Long -> java.lang.Long
* Python 3 Int -> java.lang.Long
* Float -> java.lang.Double
* List -> java.util.ArrayList
* Tuple -> Collections.unmodifiableList(ArrayList)
* Dict -> java.util.HashMap
* Callable -> jep.python.PyCallable
* numpy.ndarray -> jep.NDArray
* object -> java.lang.String (This is a last resort where ``Jep.getValue(String)``
            returns ``str(pyobject)``. Do not depend on this behavior, it will change
            in the future).

*jtypes.jep* introduced support for retrieving Python objects in Java by the addition
of the method ``Jep.getValue(String name, Class<T> desiredType)``.
By specifying a desired type, *jtypes.jep* will do its best to provide you with that
type if the type conversion to a Java object is reasonable.  *jtypes.jep* also supports
retrieving references to native Python objects by using
``Jep.getValue(name, PyObject.class)`` or ``Jep.getValue(name, PyCallable.class)``.
PyObjects in Java have the methods ``getAttr`` and ``setAttr`` to enable getting and
setting Python attributes from Java, similar to the dot ``.`` operator.
PyCallable is a subclass of PyObject and supports invoking Python methods.  For more
information, please see the `javadoc <http://ninia.github.io/jep/javadoc/3.8/>`__.

Memory usage
============

*jtypes.jep* will use both Java heap memory and native (aka direct or system) memory.
All the Java objects will use heap memory as usual, while any Python objects will use
native memory as usual.  The wrapper objects such as PyJObject will actually be using
both heap memory for the Java object and native memory for the associated pointers
and metadata of the PyJObject.

When *jtypes.jep* wraps a Java object as a PyJObject, it notifies the JVM that it holds
a reference to that Object, ensuring that the JVM will not garbage collect the object.
When the Python garbage collector detects that there are no more references to that
PyJObject (in Python at least), it will garbage collect the PyJObject wrapper.
An example of this is when a variable is defined in a method scope and goes out of
scope when the method returns/exits.  When Python garbage collects the wrapper object,
*jtypes.jep* will release the associated native memory of the PyJObject and notify
the JVM that it no longer has a reference to the object.  This then enables the JVM
to garbage collect the underlying Java object if there are no more references to it.

Another way to explain the memory management of *jtypes.jep* is to view the JVM
as delegating to Python until Python is done with the object. The Java garbage
collector defers collecting a Java object inside a Python interpreter until the
Python garbage collector collects it, at which point the Java garbage collector
then treats it as just another Java object.
