# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib.compat import *
from ...jvm.lib import annotate
from ...jvm.lib import public

from ._jobject import PyJObject

from .._java import AutoCloseable_close


@public
class PyJAutoCloseable(PyJObject):

    """jautocloseable"""

    # "jep.PyJAutoCloseable" # tp_name

    # A PyJAutoCloseable is a PyJObject that has __enter__ and __exit__
    # implemented. It should only be used where the underlying jobject
    # of the PyJObject is an implementation of java.lang.AutoCloseable.

    def __enter__(self):

        """__enter__ for Python ContextManager"""

        return self

    def __exit__(self, *exc_info):

        """__exit__ for Python ContextManager"""

        # Exits the Python ContextManager and calls
        # java.lang.AutoCloseable.close().

        del exc_info
        AutoCloseable_close(self.__javaobject__)
