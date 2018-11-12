# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib.compat import *
from ...jvm.lib import annotate
from ...jvm.lib import public


@public
class PyJMonitor(object):

    """jmonitor"""

    # "jep.PyJMonitor" # tp_name

    # A PyJMonitor is a PyObject that has __enter__ and __exit__
    # implemented to make a Python ContextManager and implement a Java
    # synchronized(Object) { ... } block. This enables Java Object locking
    # from Python using the 'with' keyword.

    @annotate(jobject='jt.jvm.JObjectBase')
    def __new__(cls, jobject):

        # Returns a new PyJMonitor, which is a PyObject that can lock with
        # Java synchronized on an object.

        self = super(PyJMonitor, cls).__new__(cls)
        self.__javaobject__ = jobject
        with self.__javaobject__.jvm as (jvm, jenv):
            # the object to lock on, e.g. synchronized(lock) { code }
            self.__lock = jenv.NewGlobalRef(self.__javaobject__.handle)

        return self

    def __del__(self):

        try: jvm, jenv = self.__javaobject__.jvm
        except: return
        if jenv:
            jenv.DeleteGlobalRef(self.__lock)

    def __enter__(self):

        """__enter__ for Python ContextManager that locks"""

        # Enters the Python ContextManager and intrinsically locks on the object.
        # Will wait for the lock if it is locked by something else, just like
        # a Java synchronized block.

        # We absolutely cannot have the GIL when we attempt to synchronize
        # on the intrinsic lock. Otherwise we can potentially deadlock if
        # this locking operation is blocked but holds the GIL while another
        # thread has the lock but is awaiting the GIL.

        with self.__javaobject__.jvm as (jvm, jenv):
            if jenv.MonitorEnter(self.__lock) < 0:
                raise Exception("??? !!!")
        return self

    def __exit__(self, *exc_info):

        """__exit__ for Python ContextManager that unlocks"""

        # Exits the Python ContextManager and releases the intrinsic lock
        # on the object.

        del exc_info
        with self.__javaobject__.jvm as (jvm, jenv):
            if jenv.MonitorExit(self.__lock) < 0:
                raise Exception("??? !!!")
