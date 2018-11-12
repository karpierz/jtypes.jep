.. _Jep-and-the-GIL:

*jtypes.jep* and the GIL
************************

What is the Global Interpreter Lock (GIL)?
==========================================

If you're looking at *jtypes.jep* as a Java developer, you might not be very familiar
with CPython's GIL. The GIL is the Global Interpreter Lock and exists `for a variety
of reasons <http://programmers.stackexchange.com/questions/186889/why-was-python-written-with-the-gil>`__.
Note that Jython and IronPython do not have a GIL, but if you're looking at *jtypes.jep*
it may be because you want to use CPython extensions.  Attempts have been made to remove
the GIL from CPython but all attempts have failed to elegantly remove it while maintaining
compatibility and meeting requirements.
So for now and the foreseeable future, the GIL is part of CPython.

How does the GIL affect Python programs?
========================================

The GIL must be acquired when interpreting Python code and manipulating Python objects,
therefore Python programs running in the CPython interpreter cannot truly be multithreaded.
However, once you dive into CPython extensions, it gets more complex and can potentially
be multithreaded.  An excellent example is numpy, which aggressively releases the GIL
when executing computations in C, enabling simultaneous thread execution. For more information,
consult the `Python wiki on the GIL <https://wiki.python.org/moin/GlobalInterpreterLock>`__.

How does *jtypes.jep* use the GIL?
==================================

*jtypes.jep* must acquire the GIL to run code in the CPython interpreter.
When *jtypes.jep* crosses natively into C and uses the CPython API, it acquires the GIL.
However, like numpy, *jtypes.jep* strategically releases the GIL when appropriate.
Specifically, every time a Java method (including constructors) is invoked from the embedded
interpreter, *jtypes.jep* will release the GIL, because *jtypes.jep* has no idea how long
that Java method may take to execute, and *jtypes.jep* is not manipulating CPython objects
during the Java code execution. After the method call returns, *jtypes.jep* must reacquire
the GIL to resume interpreting Python.

The GIL is truly global in that it is a singleton across the entire process.
Therefore multiple Jep instances/sub-interpreters may compete for the GIL and block until
they acquire it, reducing throughput of computations.

How does the GIL affect *jtypes.jep* performance?
=================================================

It depends on the specific scenario.

* If you're running with a single Jep instance or a single-threaded application,
  the GIL will be unnoticeable.
* If you're running a lot of Java Jep threads with long running Python code that is not
  invoking Java methods from Python and not using smart CPython extensions like numpy
  that release the GIL, you may suffer performance degradation.
* If you're somewhere in the middle (like most), you will hopefully not notice the GIL
  affecting performance, but it is something to keep in mind if performance becomes an issue.

How can I work around GIL performance issues?
=============================================

There's a lot of ways to approach this problem depending on the scenario.

* Verify CPython extensions release the GIL.
  If you're using a CPython extension, verify in the extension's code that any
  C libraries or methods which are not using the CPython API are releasing the GIL.
  (This is presuming the extension is safely written for multithreading).
  If the extension is not releasing the GIL and could be, consider contributing to
  open source by notifying the developers of the extension or submitting code to them.
* Port some Python code to Java.
  If some of the code does not need to be in Python, you can port it to Java, call
  the new Java method from Python, and get boosted performance.  This has two benefits.
  The first is that the GIL will be released when the Java method is invoked from Python,
  the second is that Java's JIT compiler can easily outperform Python on operations
  such as ``for`` loops.
* Try porting some of the code to `Cython <http://cython.org/>`__.
  Cython can speed up Python code noticeably, and you can even write Cython code that
  releases and reacquires the GIL appropriately. Since Cython compiles to C code compatible
  with CPython, it should work with *jtypes.jep*.
  **Disclaimer**: *Not aware of anyone trying this yet.*
* Use Python's ``multiprocessing`` module.
  For better or for worse, Python took the route of preferring multiprocessing over
  multithreading.  There is a powerful multiprocessing module you can use to spawn separate
  processes.  These spawned processes will appear as children of the original Java process,
  but they will actually be pure Python. Spawning Python subprocesses complicates things
  and requires pure Python code to be run in the separate process and sending objects
  (usually pickled/cpickled) back to the Jep interpreter running inside Java.
* Port some Python code to C.
  Python has plenty of convenient hooks for calling into C, and in the C code you can
  release and reacquire the GIL as necessary.  That said, if you're resorting to writing C,
  maybe you should just call the C code through JNI and skip *jtypes.jep* and Python.
