**Currently only as placeholder (because a base package jtypes.jvm is still in development)**

jtypes.jep
==========

Java Embedded Python.

Overview
========

  | **jtypes.jep** embeds CPython in Java.

  `PyPI record`_.

  | **jtypes.jep** is a lightweight Python package, based on the *ctypes* or *cffi* library.
  | It is an almost fully compliant implementation of Mike Johnson's **Jep** package
    by reimplementing its functionality in a clean Python instead of C.

About Jep:
----------

Borrowed from the `original website`_:

  **Jep** embeds CPython in Java through JNI and is safe to use in a heavily
  threaded environment. 

  Some benefits of embedding CPython in a JVM:

  * Using the native Python interpreter may be much faster than alternatives.
  * Python is mature, well supported, and well documented.
  * Access to high quality Python modules, both native CPython extensions and
    Python-based.
  * Compilers and assorted Python tools are as mature as the language.
  * Python is an interpreted language, enabling scripting of established
    Java code without requiring recompilation.
  * Both Java and Python are cross platform, enabling deployment to different
    operating systems.

  Notable features

  * Interactive Jep console much like Python's interactive console
  * Supports multiple, simultaneous, mostly sandboxed sub-interpreters
  * Numpy support for Java primitive arrays

Requirements
============

- Java >= 1.7 - either the Sun/Oracle JRE/JDK or OpenJDK.
- NumPy >= 1.7 (optional)

Installation
============

Prerequisites:

+ Python 2.7 or higher or 3.4 or higher

  * http://www.python.org/
  * 2.7 and 3.6 are primary test environments.

+ pip and setuptools

  * http://pypi.python.org/pypi/pip
  * http://pypi.python.org/pypi/setuptools

To install run::

    python -m pip install --upgrade jtypes.jep

To ensure everything is running correctly you can run the tests using::

    python -m jt.jep.tests

Development
===========

Visit `development page`_

Installation from sources:

Clone the `sources`_ and run::

    python -m pip install ./jtypes.jep

or on development mode::

    python -m pip install --editable ./jtypes.jep

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install tox

License
=======

  | Copyright (c) 2014-2018 Adam Karpierz
  |
  | Licensed under the zlib/libpng License
  | http://opensource.org/licenses/zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>

.. _PyPI record: https://pypi.python.org/pypi/jtypes.jep
.. _original website: https://github.com/ninia/jep
.. _development page: https://github.com/karpierz/jtypes.jep
.. _sources: https://github.com/karpierz/jtypes.jep
