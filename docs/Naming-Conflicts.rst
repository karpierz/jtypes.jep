.. _Naming-Conflicts:

Naming Conflicts
****************

Python Keywords
===============

It is impossible to directly access java methods and fields from python if the name
is the same as a python keyword. For example, in python 2, ``print`` is a keyword in python
so the python interpreter will not allow object attributes named ``print`` so the following
code will not work as expected:

.. code-block:: python

   from java.lang import System
   System.out.print("Hello")

You can work around this limitation by using ``getattr`` to access the ``print`` method
like this:

.. code-block:: python

   from java.lang import System
   getattr(System.out, "print")("Hello")

Here are all the keywords currently reserved by python, all of these keyword will have
the same problems if they are used as field or method names on java objects.

::

   False     class     exec      in        print
   None      continue  finally   is        raise
   True      def       for       lambda    return
   and       del       from      nonlocal  try
   as        elif      global    not       while
   assert    else      if        or        with
   break     except    import    pass      yield

Python Packages
===============

When a java package and a python module have the same prefix then you will not be able
to use both from within the same jep interpreter. For example it is not possible to use
both the ``io.netty`` java package and the ``io`` module from the same interpreter.
This behavior is controlled by the ``ClassEnquirer`` which is passed into jep instance.
The default ClassEnquirer will allow any java packages on the classpath to override python
packages. Default ClassEnquirer will ignore java packages that start with ``io`` and ``re``
since these are common python modules and uncommon java prefixes
(see `#29 <https://github.com/ninia/jep/issues/29>`__).
