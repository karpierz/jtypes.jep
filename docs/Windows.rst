.. _Windows:

Windows
*******

Build Setup
===========

Special thanks goes to David Lovely, Günther Weidenholzer, and Nikolas Falco
for getting variations of the Windows build working and sharing their notes and experience.

CPython extensions generally need to be built with the same compiler that built Python.
That's usually MSVC, and MSVC needs to be installed prior to building *jtypes.jep*,
but sadly it's not that simple.  You must build with very specific versions of MSVC for
this to work correctly, and you may need to install extra packs if you want 64-bit.

Any deviation from this (i.e. MinGW or a different version of MSVC) is at your own risk.
If you manage to successfully build with variations **and** have a working and stable
*jtypes.jep*, we'd love to hear about it.  The following steps presume you allow MSVC
to install to its default directories.  If you install MSVC elsewhere, you may have to
slightly alter steps that mention specific paths.

The steps to build are rather specific based on the compiler.
We recommend you don't have all these compilers installed simultaneously, if you need
something like that, virtual machines are the way to go.
`This Python page <https://wiki.python.org/moin/WindowsCompilers>`__ may prove helpful
in finding the right compiler.

 * :ref:`Python 2.7 setup <python-27-msvc-build-setup>`
 * :ref:`Python 3.3 and 3.4 setup <python-33-and-34-msvc-build-setup>`
 * :ref:`Python 3.5 and 3.6 setup <python-35-and-36-msvc-build-setup>`

Python 2.7 MSVC++ Build Setup
-----------------------------

This is the easiest way to build *jtypes.jep* with Python 2.7 for Windows.
Microsoft released a compiler specifically for building Python and CPython
extensions with Python 2.7. The compiler is freely available and known as the
`Microsoft Visual C++ Compiler for Python 2.7
<http://www.microsoft.com/en-us/download/details.aspx?id=44266>`__.
Thankfully this compiler supports both 32-bit and 64-bit.
After downloading and installing the compiler, skip down to the
:ref:`Running the build <running-the-build>` step.

.. _python-27-msvc-build-setup:

Python 2.7 MSVC Build Setup
---------------------------

The `official Python 2 <https://www.python.org/downloads/>`__ was built with Microsoft
Visual Studio Express 2008, so that's the official way to build *jtypes.jep* for Python 2.
The compiler is freely available and also known as MSVC 9.0. You will need to download
and install it. Finding a download link can be difficult, here is one that is working:

* http://go.microsoft.com/?linkid=7729279

If you want to build 32-bit, skip down to the :ref:`Running the build <running-the-build>`
step.

----

If you want to build 64-bit, continue on with these steps:

1. You need to download and install the `Microsoft Windows SDK for Windows 7 and .NET
   Framework 3.5 SP1 <http://www.microsoft.com/en-us/download/details.aspx?id=3138>`__.
   It is very important that you use this download with .NET Framework 3.5,
   the installer with .NET Framework 4 will not work as it assumes Visual Studio 2010.

2. When you run the installer, it will prompt you about what to install.
   You need to install the following:

   * Windows Headers and Libraries
   * Visual C++ Compilers
   * Win32 Development Tools (under Windows Development Tools)

3. Copy ``C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\bin\vcvars64.bat``
   to   ``C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\bin\amd64\vcvarsamd64.bat``.

4. Proceed to the :ref:`Running the build <running-the-build>` step.

.. _python-33-and-34-msvc-build-setup:

Python 3.3 and 3.4 MSVC Build Setup
-----------------------------------

The `official Python 3.3 and Python 3.4 <https://www.python.org/downloads/>`__ were built
with Microsoft Visual Studio Express 2010, so you should build *jtypes.jep* with that.
It is freely available and also known as MSVC 10.0.  You will need to download
and install it. Finding a download link can be difficult, here is one that is working:

* http://microsoft-visual-cpp-express.soft32.com/

If you want to build 32-bit, skip down to the :ref:`Running the build <running-the-build>`
step.

----

If you want to build 64-bit, continue on with these steps:

1. You need to download and install the `Microsoft Windows SDK for Windows 7 and
   .NET Framework 4 <http://www.microsoft.com/en-us/download/details.aspx?id=8279>`__.
   It is very important that you use this download with .NET Framework 4, the installer
   with .NET Framework 3.5 will not work as it assumes Visual Studio 2008.

2. When you run the installer, it will prompt you about what to install.
   You need to install the following:

   * Windows Native Code Development

     * Windows Headers and Libraries
     * Tools
     * Visual C++ Compilers

3. You can't build *jtypes.jep* 64-bit with an ordinary command prompt. Instead go to
   ``Start -> All Programs -> Microsoft Windows SDK 7.1 -> Windows SDK 7.1 Command Prompt``.

4. Proceed to the :ref:`Running the build <running-the-build>` step.

.. _python-35-and-36-msvc-build-setup:

Python 3.5 and 3.6 MSVC Build Setup
-----------------------------------

The `official Python 3.5 and Python 3.6 <https://www.python.org/downloads/>`__
were built with Microsoft Visual C++ 2015 Build Tools, Microsoft Visual Studio 2015,
or Microsoft Visual Visual Studio 2017, so you should build Jep with one of those.
The compiler is freely available and also known as MSVC 14.0.
You will need to download and install it, the easiest one to use is
Microsoft Visual C++ 2015 Build Tools.  Here are some download links:
* https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
* http://landinghub.visualstudio.com/visual-cpp-build-tools

Note we have not tried building 32-bit Jep on Windows with Python 3.5 and 3.6.
You may or may not need to do the following steps.

----

If you want to build 64-bit, continue on with these steps:

1. You need to download and install the `Microsoft Visual C++ 2015 Build Tools
   <http://landinghub.visualstudio.com/visual-cpp-build-tools>`__.

2. When you run the installer, it will prompt you about what to install.
   You need to install the following:

   * Windows 8.1 SDK
   * Windows 10 SDK

3. Proceed to the :ref:`Running the build <running-the-build>` step.

.. _running-the-build:

Running the build
-----------------

Presuming you completed the steps above for your version of Python, you should be ready
to build *jtypes.jep*.  You might want to make a **virtualenv** to keep things isolated,
and if you wanted **numpy** support you should install it now if it's not already installed.
An easy way to get a numpy install working on Windows is to download a wheel from this page:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

If you want to install the numpy wheel, use ``python -m pip install path/to/wheelfile.whl``.
If you're using virtualenv, make sure you run the pip command after you've activated
the virtualenv so numpy installs to the virtualenv.

**To run the build**, from the jep dir use ``python setup.py build``.
If all goes well you will end up with a build dir with some jars, jep.dll, jep.bat,
and a few other files.  Running ``python setup.py test`` will let you run the unit tests.
Running ``python setup.py install`` will place the files in their appropriate locations:

* Python's Lib/site-packages/jep directory

  * jep \*.py files
  * jep jar file
  * jep.dll

* Python's Scripts directory

  * jep.bat

If you'd like further testing, simply run the jep.bat file to use the interactive interpreter.

Further Help
------------

Should you diverge from this path, or get stuck, someone else may have run into the same
problems as you.  The following Stack Overflow pages are quite useful for trying to build
CPython extensions on Windows:

* http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat
* http://stackoverflow.com/questions/13596407/errors-while-building-installing-c-module-for-python-2-7
* http://stackoverflow.com/questions/23691564/running-cython-in-windows-x64-fatal-error-c1083-cannot-open-include-file-ba

Other Insights
~~~~~~~~~~~~~~

The ``setup.py build`` command should produce a jep.dll file (because the library will be
loaded from Java, we need a DLL).
The DLL will retain a manifest in the file so the operating system can load it correctly.
The ``setup.py install`` command should only install the jep.dll file.
