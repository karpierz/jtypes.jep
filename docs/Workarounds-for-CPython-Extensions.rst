.. _Workarounds-for-CPython-Extensions:

Workarounds for CPython Extensions
**********************************

Background
==========

*jtypes.jep* doesn't work correctly with some CPython extensions due to how those extensions
were coded.  Oftentimes projects were not designed towards the idea of running in embedded
sub-interpreters instead of in a standard, single Python interpreter. When running *jtypes.jep*,
these types of problems have been known to appear as a JVM crash, an attribute inexplicably
set to ``None``, or a thread deadlock.

Most of these errors can be traced to the CPython extension using global static variables
that are not sandboxed to a sub-interpreter, and therefore behave erroneously when running
in a multi-threaded or multi-interpreter environment.  In these cases, it's good practice
to try and track down the error and identify it to the project maintainers so they are
at least aware of the problem.  There's not much *jtypes.jep* can do to ensure that these
other modules work correctly in a multi-threaded, embedded, sub-interpreter environment.

Workarounds
===========

There are workarounds when using *jtypes.jep* that can potentially enable an application
to use the functionality of the CPython extension while dodging errors:

#. Use SharedInterpreter rather than a plain *jtypes.jep* instance.
   Shared interpreters avoids the use of sub-interpreters so it is more like the environment
   that extensions are usually tested with.
#. Include the CPython extension in the set of shared modules when you create a Jep instance.
   This solves problems that can arise if the extension is initialized more than once.
#. Use a singleton Jep instance.  This prevents other sub-interpreters in the same process
   from messing up the C variables.  You can potentially use the singleton instance for that
   one module and have multiple sub-interpreters for other pure Python code.
#. Use thread pools to reuse Jep instances and never close those Jep instances.
   This prevents errors where the module's methods or attributes may be garbage collected or
   reset when a sub-interpreter shuts down.
#. Synchronize on *jtypes.jep* calls into Python that use the module.
   If the module is not thread safe, you can still attempt multiple sub-interpreters and
   synchronize when using Python that uses that module.
