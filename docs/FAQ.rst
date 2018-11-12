.. _FAQ:

Frequently Asked Questions
**************************

What Python modules does *jtypes.jep* work with?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* *jtypes.jep* should work with any pure Python modules.
  CPython extensions and Cython modules may or may not work correctly,
  it depends on how they were coded.  There are various techniques to try and overcome
  some of the complications of CPython extensions, please see the
  :ref:`Workarounds for CPython Extensions <Workarounds-for-CPython-Extensions>` page.

Does Jep work with CPython extension?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* *jtypes.jep* works with a variety of CPython extensions.  Developers have reported that
  *jtypes.jep* works with **numpy**, **scipy**, **pandas**, **tensorflow**, **matplotlib**,
  **cvxpy**, and more.
  Please let us know what other CPython extensions you are using with Jep or update this list.

Is *jtypes.jep* a good fit for my project?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* That's a complex question. It depends on your project's requirements, but here's a
  simplification of the question. Do you want to run a Java process or a Python process?

  * **Java**

    * Do you need to use CPython modules (e.g. numpy)?

      * **Yes**: *jtypes.jep* is a good fit because we strive to work well with native CPython
        modules. `jpy <https://github.com/bcdev/jpy>`__ and `JyNI <http://jyni.org/>`__ are
        alternatives with support for native modules.
      * **No**: `Jython <http://www.jython.org/>`__ is typically used but *jtypes.jep* will
        work well regardless of if you use native modules or not.

  * **Python**

    * Sinces *jtypes.jep* embeds CPython, it can run Python code just like other Python
      interpreters. But it cannot be launched from a Python process (*we may add this
      in the future*). If you want access to Java from a Python process, consider
      the following projects:

      * `JPype <http://jpype.sourceforge.net/>`__

        * `JPype forked <https://github.com/originell/jpype>`__

      * `Pyjnius <https://pyjnius.readthedocs.org/en/latest/>`__
      * `Py4J <https://www.py4j.org/>`__
      * `jpy <https://github.com/bcdev/jpy>`__

How do I fix Unsatisfied Link Error: no jep in java.library.path?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* This error informs you that the Java process cannot find *jtypes.jep*'s built C library.
  The name of the library is somewhat platform dependent, it is usually **libjep.so** on
  Linux, **libjep.jnilib** on OS X, and **jep.dll** on Windows.
  There are a few different ways to fix the problem:

  1. Place the shared library where Python has its other shared libraries.
     This is usually python/lib with \*nix systems and python/dlls with Windows systems.

  2. Set an environment variable that tells Java the directory of the *jtypes.jep*
     shared library.

    * On Linux, set ``LD_LIBRARY_PATH``.
    * On OS X, set ``DY_LD_LIBRARY_PATH``.
    * On Windows, set ``PATH``.

  3. Pass the argument ``-Djava.library.path`` to your Java process with the location of the
     *jtypes.jep* shared library.

  4. *jtypes.jep* will try harder to find the native library for you if you set the PYTHONHOME
     environment variable.

* See http://stackoverflow.com/questions/20038789/default-java-library-path for more information.

Does *jtypes.jep* work on Android?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* We haven't tried it yet.
  In theory it should possible, but there may be some challenges to overcome.
  If you try this, we'd love to hear about it and will gladly accept contributions
  to make *jtypes.jep* work well on more platforms.

Is *jtypes.jep* available through Maven?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The jars are available through Maven, the native library is not.
  Look at the `pom.xml <https://github.com/ninia/jep/blob/master/pom.xml>`__ file
  to find the groupId is black.ninia and the artifactId is jep.

What Java UI frameworks does *jtypes.jep* support?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* *jtypes.jep* has been run with Swing and SWT.
  We haven't tried JavaFX yet.

Does *jtypes.jep* work with OSGi?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Yes.

Why does ``eval(String)`` return a boolean instead of an Object of the result?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``eval(String)`` was originally written to support interactive mode or non-interactive mode
  (multiple statements or a single statement, see javadoc), so the boolean return value
  is whether or not the statement was actually executed.  There is also an overhead of always
  returning the result, especially if code is making multiple calls to eval(String) and doesn't
  need the results.  To change the method signature now would potentially break compatibility
  with a number of applications.

* ``getValue(String)`` is almost identical in the C code to ``eval(String)`` and will return
  the result of the evaluation, and can be used instead of eval where desired. For example:

.. code-block:: java

   // evaluates and discards the result
   jep.eval("2 + 4");

   // evaluates and places the results in x
   jep.eval("x = 2 + 4");
   Integer x = (Integer) jep.getValue("x");

   // evaluates and returns the results
   Integer y = (Integer) jep.getValue("2 + 4");

How do I fix Fatal Python Error when *jtypes.jep* starts up?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If you see fatal Python errors when first using *jtypes.jep*, that often implies the
  ``PATH`` or ``LD_LIBRARY_PATH`` environment variables are incorrect or inconsistent.
  This is often seen if multiple versions of python are installed and/or *jtypes.jep*
  was built with a different version of Python than it is running with.

Does *jtypes.jep* work with alternative Python distributions such as Anaconda, PyPy, Stackless, or Jython?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* *jtypes.jep* is only officially supported and routinely tested using the CPython reference
  distribution. There are just too many different combinations of Java, Python, and OS variants
  to be able to support them all. For Windows and OS X the version available for download from
  www.python.org is used in development and testing. The default Python on most \*nix variants
  is almost always a compatible CPython build.

  * Many Jep users have reported *jtypes.jep* works with Anaconda.

* Other versions of Python may work but they do not receive routine testing and they may require
  additional effort to ensure that the correct versions of all native libraries can be loaded.
  If you are having trouble you can try Google or the
  `Mailing List <https://groups.google.com/d/forum/jep-project>`__ to see if there are other
  users with a similar setup. Please do not report errors related to the build or loading of
  libraries on the github issue tracker since it is unlikely that *jtypes.jep* will change
  to support these variants unless you can provide a patch to do so.

Does *jtypes.jep* work with Scala?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Yes.

Can I start new Python threads from *jtypes.jep*?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Yes, however there are currently a few limitations
  1. You must ensure that all Python threads have completed before closing *jtypes.jep*.
  2. You cannot access Java from any new Python threads.
