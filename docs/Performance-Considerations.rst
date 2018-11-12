.. _Performance-Considerations:

Performance Considerations
**************************

Jep is used on production systems that run significant amounts of Python in servers
aiming for 99.999% uptime. In these situations there are some recommended best practices.

Memory management
=================

You can leak Python objects (*or Java objects in Python!*) if you continually create
new variables in a sub-interpreter's global scope.  There's a few different techniques
you can use to ensure this doesn't happen.  In no particular order:

* Execute most of your Python code in functions, so any variables created exist only
  temporarily in local scope.  The Python garbage collector will take care of variables
  after they go out of scope.  For example:

.. code-block:: python

   def foo():
       args = get_args()
       values = pre_process(args)
       doMath(values)

.. code-block:: java

   jep.eval("foo()");

where foo() does all the work.
args and values will go out of scope and be automatically cleaned up.

* Delete any variables created by ``jep.set(String name, Object var);`` once you are
  done with them.  For example:

.. code-block:: java

   jep.set("x", javaObj);
   jep.eval("result = foo(x)");
   Object result = jep.getValue("result");
   jep.eval("del x");
   jep.eval("del result");

You can also shortcut this with Python code like:

.. code-block:: python

   for g in globals():
      if some_condition(g):
         del g

* Close the Jep interpreters when you are done with them.  For example:

.. code-block:: java

   Jep jep = null;
   try
   {
       jep = new Jep();
       // runScript, invoke, eval, and other fun things
   } finally {
       if (jep != null) {
           jep.close();
       }
   }

With Java 7 it's even easier:

.. code-block:: java

   try (Jep jep = new Jep())
   {
      // runScript, invoke, eval, and other fun things
   }

Speed
=====

Starting and stopping Python sub-interpreters, while fast, is relatively slow in comparison to
using an already initialized sub-interpreter.  This becomes even more noticeable as the number
of modules that get imported into the sub-interpreter grows.  In these cases you should strongly
consider retaining your Jep instances (ie Python sub-interpreters) and reusing them.

See also :ref:`Jep and the GIL <Jep-and-the-GIL>`.

Efficiency
==========

*jtypes.jep* requires that the thread that initializes the sub-interpreter is the same thread
for any operations on the sub-interpreter. If you want to reuse Jep instances for speed or
stateful reasons, and you also want to multithread your calls to Python, a useful technique
is to pool Jep instances/Python sub-interpreters.  An accompanying factory class can create and
initialize your Jep instances on demand for the pool, and you can limit the number of threads
in the pool to ensure that the Python components do not overwhelm the rest of the system.
