.. _Exception-Handling:

Exception Handling
******************

Uncaught Exceptions
===================

The *jtypes.jep* frequently checks for exceptions to prevent the native code
from getting in a bad state. When an uncaught exception is encountered:

#. *jtypes.jep* creates a new JepException. If the exception was a Java exception,
   the cause will be the original Java exception.
#. *jtypes.jep* attempts to use the traceback module to build a stack trace of the
   Python code. If successful, it will use the Python traceback information to emulate
   Java StackTraceElements for a more complete picture of the trace to the error.
#. *jtypes.jep* will then throw the JepException out of the interpreter back to the
   calling Java code.

Catching Java exceptions in Python
==================================

If Java code invoked from Python throws an exception of one of a few select types,
you can catch the exception in Python if desired.  For example:

.. code-block:: python

   try:
      # throws ClassNotFoundException
      from java.lang import ArrayList
   except ImportError as ie:
      from java.util import ArrayList

The Java types that support this with their equivalent Python exceptions are:

* ClassNotFoundException -> ImportError
* IndexOutOfBoundsException -> IndexError
* IOException -> IOError
* ClassCastException -> TypeError
* IllegalArgumentException -> ValueError
* ArithmeticException -> ArithmeticError
* OutOfMemoryError -> MemoryError
* AssertionError -> AssertionError

All other Java exceptions will be treated by the *jtypes.jep* as RuntimeErrors.
