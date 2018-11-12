.. _Getting-Started:

Getting Started
***************

Dependencies
============

*jtypes.jep* requires that the following dependencies be installed before it can be built and run:

* JRE >= 1.7
* Python >= 2.7 or Python >= 3.4

Building *jtypes.jep*
=====================

If you cloned or downloaded the *jtypes.jep* source, you will need to build *jtypes.jep*.
Simply run:

    python setup.py build

If the build succeeds it will create a directory jep/build which will contain a jep.jar and
the compiled C library of *jtypes.jep*, typically named jep.so or jep.dll depending on your
platform.

Installing *jtypes.jep*
=======================

There are multiple ways to install *jtypes.jep*, in order of least involved to most involved:

1. If you used *python -m pip install jtypes.jep*, *jtypes.jep* should already be built
   and installed.
2. If you built the source yourself, you can run *python setup.py install* to install
   *jtypes.jep* to the standard dirs.
3. If you would like to include jep as part of your application, you can place the files
   as necessary presuming the following conditions are met:

  * The jep.jar is accessible to the Java classloaders (typically through the Java classpath)
  * The shared library (jep.so or jep.dll) is accessible by the Java process (typically through
    -Djava.library.path or the environment variable LD_LIBRARY_PATH)
  * The jep python files (console.py, java_import_hook.py, version.py, etc) are accessible by
    Python (typically by placing them in the site-packages/jep directory).

Example Code
============

Using *jtypes.jep* in your application is designed to be easy to intermix Java and Python
objects in the Python interpreter.

**Hello World**

.. code-block:: java

   try (Jep jep = new Jep())
   {
       jep.eval("from java.lang import System");
       jep.eval("s = 'Hello World'");
       jep.eval("System.out.println(s)");
       jep.eval("print(s)");
       jep.eval("print(s[1:-1])");
   }

**Calling Python methods from Java and getting results**

.. code-block:: java

   try (Jep jep = new Jep())
   {
       jep.eval("import somePyModule");
       // any of the following work, these are just pseudo-examples

       // using eval(String) to invoke methods
       jep.set("arg", obj);
       jep.eval("x = somePyModule.foo1(arg)");
       Object result1 = jep.getValue("x");

       // using getValue(String) to invoke methods
       Object result2 = jep.getValue("somePyModule.foo2()");

       // using invoke to invoke methods
       jep.eval("foo3 = somePyModule.foo3")
       Object result3 = jep.invoke("foo3", obj);

       // using runScript
       jep.runScript("path/To/Script");
   }

**Calling Java constructors from Python**

.. code-block:: python

   # importing the java.lang.Class objects
   from java.util import HashMap
   from java.util import ArrayList as AL

   # instantiation
   x = HashMap()
   y = HashMap(100)
   a = AL()

**Calling Java methods from Python**

.. code-block:: python

   from java.util import ArrayList, HashMap

   a = ArrayList()
   a.add("abc")
   a += "def"
   print(a)

   m = HashMap()
   m.put("listkey", a)
   m["otherkey"] = "xyz"
   print(m)
