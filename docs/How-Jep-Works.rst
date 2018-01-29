.. _How-Jep-Works:

How *jtypes.jep* Works
**********************

Basics
======

*jtypes.jep* uses JNI and the CPython API to start up the Python interpreter inside
the JVM. The initial top-level interpreter will never be used except to initialize
and shut down Python. When you create a Jep instance in Java, a sub-interpreter
will be created for that Jep instance and will remain in memory until the Jep instance
is closed with jep.close(). The initial top-level interpreter will remain in the JVM
until the JVM exits.

Sandboxed interpreters
======================

Each Jep instance's sub-interpreter is sandboxed apart from the other sub-interpreters.
This means a change to the imported modules, global variables, etc in one interpreter
will not be reflected in other sub-interpreters. However, this rule does not apply to
CPython extensions.  There is no way to strictly enforce a CPython extension is
implemented in a way that supports sandboxing.
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

Threading complications
=======================

Due to complications and limitations of JNI, a thread that creates a Jep instance must
be reused for all method calls to that Jep instance. *jtypes.jep* will enforce this and
throw exceptions mentioning invalid thread access.
(*In the future we hope to simplify or provide utilities for thread management*).

More than one Jep instance should not be run on the same thread at the same time.
While this is technically allowed, it can potentially mess up the thread state and
lead to deadlock in the Python interpreter.
This will probably be changed to throw an exception if encountered in the future.

Objects
=======

*jtypes.jep* will automatically convert Java primitives, Strings, and jep.NDArrays sent
into the Python sub-interpreter into Python primitives, strings, and numpy.ndarrays
respectively. The Python versions of these objects will have no reference to their
original Java counterparts, they are entirely new objects that exist solely in Python's
system memory.

A Java object that does not match one of the types listed above will automatically
be wrapped as a PyJObject (or one of its related classes).
A PyJObject wraps the reference to the original Java object and presents the Python
sub-interpreter with an interface for understanding the object as a Python object.
From the point-of-view of the Python sub-interpreter, a PyJObject is just another
Python object with a select set of attributes (fields and methods) on it.

Currently *jtypes.jep* does not have as strong of support for manipulating Python
objects with Java code.  Python strings, primitives, and numpy.ndarrays will be
automatically converted to their Java equivalent when passed/returned to Java.
These Java objects will be equivalent copies, not references to the Python objects.
``Jep.getValue(String)`` has added support for other standard Python types such as
lists, tuples and dictionaries.  Invoking a Java method from Python, such as
``result = javaObj.foo(arg1, arg2, arg3)``, is not as tolerant of Python objects as
``Jep.getValue(String)``.
*jtypes.jep* must attempt to match the method signature with the arguments and
therefore cannot be as lenient with regards to the Python type of the argument.
(*We aim to improve this in a future release*).

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
collector defers collecting a Java object inside a Python sub-interpreter until
the Python garbage collector collects it, at which point the Java garbage collector
then treats it as just another Java object.
