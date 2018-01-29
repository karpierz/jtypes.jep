.. _OS-X:

OS X
****

Build
=====

The OS X build requires Xcode.  In recent versions of OS X, running the build
will automatically prompt you to download Xcode if it is not found.

For a permanent install on OS X, Apple recommends placing JNI libraries at
``/Library/Java/Extensions/``.
For that case, you can link libjep.so there such as
``ln -sf libjep.so /Library/Java/Extensions/libjep.jnilib``.
