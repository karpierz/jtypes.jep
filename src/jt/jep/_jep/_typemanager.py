# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib.compat import *
from ...jvm.lib import annotate
from ...jvm.lib import public

from ._typehandler import *  # noqa


@public
class TypeManager(object):

    __slots__ = ('_state', '_object_handlers', '_array_handlers')

    def __init__(self, state=None):

        super(TypeManager, self).__init__()
        self._state           = state
        self._object_handlers = {}
        self._array_handlers  = {}

    def start(self):

        self._register_handler(VoidHandler)
        self._register_handler(BooleanHandler)
        self._register_handler(CharHandler)
        self._register_handler(ByteHandler)
        self._register_handler(ShortHandler)
        self._register_handler(IntHandler)
        self._register_handler(LongHandler)
        self._register_handler(FloatHandler)
        self._register_handler(DoubleHandler)
        self._register_handler(StringHandler)
        self._register_handler(ClassHandler)

    def stop(self):

        self._object_handlers = {}
        self._array_handlers  = {}

    def _register_handler(self, hcls):

        thandler = hcls(self._state)
        self._object_handlers[thandler._jclass] = thandler
        return thandler

    def get_handler(self, jclass):

        if jclass.isArray():
            thandler = self._array_handlers.get(jclass)
            if thandler is None:
                self._array_handlers[jclass] = thandler = ArrayHandler(self._state, jclass)
        else:
            thandler = self._object_handlers.get(jclass)
            if thandler is None:
                self._object_handlers[jclass] = thandler = ObjectHandler(self._state, jclass)
        return thandler
