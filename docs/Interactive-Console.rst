.. _Interactive-Console:

Interactive Console
*******************

Running the jep script
======================

The ``setup.py`` script will provide a ``jep`` or ``jep.bat`` script to make
launching *jtypes.jep* easier. The jep script is very similar to running ``python``
from a terminal/command line.  If run with an argument of a file path, it will run
the script at that path.  If run with no arguments, it will provide an
interactive console that combines the Python language with access to Java
classes on the classpath and in the JRE.

.. code-block:: python

   $ jep
   >>> from java.lang import System
   >>> System.out.println('hello, world')
   hello, world
   >>>

readline support
================

The jep script will attempt to use readline to remember previous commands.
If readline is supported, you can press the up arrow key ↑ to cycle through commands
from a previous jep session.  If readline is not supported, the script will print
an informative message and you can continue on without this functionality.

For Windows, you will need `pyreadline <https://github.com/pyreadline/pyreadline>`__
to enable the ability to remember commands from a previous jep session.
Make sure you get the latest pyreadline, preferably from their master branch on github,
and **not** from the pypi website (and therefore **not from pip**).
