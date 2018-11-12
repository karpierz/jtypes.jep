# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import

import sys

from ..jvm.lib import public


@public
class StdOutToJava(object):

    """Redirects Python's sys.stdout to Java's System.out"""

    def __init__(self):

        from java.lang import System
        self.oldout = sys.stdout
        self.printmethod = getattr(System.out, "print")
        self.flushmethod = getattr(System.out, "flush")

    def write(self, msg):

        self.printmethod(msg)

    def flush(self):

        self.flushmethod()


@public
class StdErrToJava(object):

    """Redirects Python's sys.stderr to Java's System.err"""

    def __init__(self):

        from java.lang import System
        self.olderr = sys.stderr
        self.printmethod = getattr(System.err, "print")
        self.flushmethod = getattr(System.err, "flush")

    def write(self, msg):

        self.printmethod(msg)

    def flush(self):

        self.flushmethod()


@public
def setup():

    sys.stdout = StdOutToJava()
    sys.stderr = StdErrToJava()
