.. _Numpy-Usage:

Numpy Usage
***********

Java primitive arrays <-> numpy.ndarrays
========================================

*jtypes.jep* supports automatic conversion of Java primitive arrays to numpy.ndarrays.
For ease and speed of copying the arrays between the two languages, the Java arrays
must be one dimensional. This is to ensure a contiguous block of a known size of
memory for the conversion. Conceptually the Java array can be n-dimensional with
the dimensions argument, but in memory it must be one dimensional.

Sending a Java primitive array into Python as a ``numpy.ndarray`` is easy using
the class ``jep.NDArray``.  For example:

.. code:: java

   try (Jep jep = new Jep(new JepConfig().addSharedModules("numpy"))
   {
       float[] f = new float[] { 1.0f, 2.1f, 3.3f, 4.5f, 5.6f, 6.7f };
       NDArray<float[]> nd = new NDArray<>(f, 3, 2);
       jep.set("x", nd);
   }

Inside the interpreter, the variable named x will be a ``numpy.ndarray`` with
shape (3,2) and dtype float32.  If a Java method signature contains an ``NDArray``,
it will also be transformed when crossing between the languages.  For example:

.. code:: java

   /**
    * If Python invokes this method, it will receive back a numpy.ndarray.
    */
   public NDArray<?> getRawData()
   {
       // presuming this.rawdata is conceptually only 1-dimensional
       return new NDArray(this.rawdata, this.rawdata.length);
   }

.. code:: java

   /**
    * If Python invokes this method, it should pass in a numpy.ndarray.
    */
   public void setData(NDArray<?> dataFromPython)
   {
       // ignoring dimensions, presuming this.rawdata is conceptually only 1-dimensional
       this.rawdata = dataFromPython.getData();
   }

At times *jtypes.jep* will convert a ``numpy.ndarray`` into a Java primitive array when
the class ``NDArray`` does not fit a method signature.  For example,

.. code:: java

   public void setFloatData(float[] dataFromPython)
   {
       // note that the dimensions are lost
       this.rawdata = dataFromPython;
   }

In this scenario the information about the ndarray dimensions will not be sent along.

Direct memory support
=====================

*jtypes.jep* does not support direct memory sharing between numpy and Java, therefore
changes in the array in one language are **not** reflected in the array in the other
language. Currently all numpy <-> Java operations are completed with a memcpy().
(*Direct memory is coming soon, it is available in the dev_3.7 branch*).

Numpy gotchas
=============

Numpy currently does not support running in an embedded interpreter, though it mostly
works. You can use the shared modules capability of *jtypes.jep* to work around the known issues.

Known issues:

* `~~Closing a Jep instance/sub-interpreter breaks some numpy methods~~
  <https://github.com/ninia/jep/issues/28>`__.
  This is the infamous *'NoneType' object is not callable* error.
  You can work around this by using the shared modules capability,
  or by never disposing a Jep sub-interpreter that has imported numpy.

* `Printing arrays sometimes fails <https://github.com/numpy/numpy/issues/3961>`__.
  Like the above issue, you can work around it by using shared modules
  or never disposing a Jep sub-interpreter that has imported numpy.

* `Floating point errors can deadlock <https://github.com/numpy/numpy/issues/5856>`__.
  You should not be able to get this error if you do not have two active
  Jep sub-interpreters on the same thread at the same time.
  *jtypes.jep* will explicitly warn you about unsafe threading in this scenario.

* `Tiny memory leak <https://github.com/numpy/numpy/issues/5857>`__.
  The leak, if it still exists in current versions of numpy, is tiny.
  It was first noticed on much older versions of numpy.
  We are still trying to prove it and track it down.
