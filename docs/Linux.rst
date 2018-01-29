.. _Linux:

Linux
*****

Required packages
=================

Regardless of operating system, *jtypes.jep* requires compatible versions of the JDK and Python
to be installed before it can be built and run.  Here are some frequently used package names:

**CentOS/RHEL**

* JDK

  * java-1.7.0-openjdk-devel
  * java-1.8.0-openjdk-devel
  * `Oracle JDK <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`__

* Python

  * python-devel

**Ubuntu/Debian**

* JDK

  * openjdk-7-jdk
  * openjdk-8-jdk
  * `Oracle JDK <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`__

* Python

  * python-dev
  * python3-dev


LD_PRELOAD
==========

Due to some (common) difficulties with Java and C projects that dlopen libraries, you may need
to set the ``LD_PRELOAD`` environment variable. That's in addition to setting ``LD_LIBRARY_PATH``
if you've installed libjep into a directory not cached by ld.so.
See the contents of the installed ``jep`` script for an example how to do this.
The script should have the correct values for your interpreter and virtualenv (if present).

``LD_PRELOAD`` only applies to \*nix systems, not Windows or OS X.  It may or may not be required
depending on your \*nix system and environment.
