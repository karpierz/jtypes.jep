# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib.compat import *
from ...jvm.lib import annotate
from ...jvm.lib import public
from ...jvm.lib import cached

from ._constants  import EJavaType
from ._constants  import EJavaModifiers
from ._constants  import EMatchType
from ._jobject    import PyJObject
from ._exceptions import TypeError
from .            import _util as util


@public
class PyJField(obj):

    """jfield"""

    # "jep.PyJField" # tp_name
    # Equivalent of: jt.JavaField

    # Represents a java field on a java object and allows getting and
    # setting values

    @annotate(field='jt.jvm.JField')
    def __new__(cls, field):

        self = super(PyJField, cls).__new__(cls)
        self.__jfield    = field  # jt.jvm.JField
        self.__is_static = False
        self.__thandler  = None
        return self

    @cached
    def __init(self):

        type_manager = self.__jfield.jvm.type_manager
        mods = self.__jfield.getModifiers()
        self.__is_static = EJavaModifiers.STATIC in mods
        self.__thandler  = type_manager.get_handler(self.__jfield.getType())

    @annotate(this=PyJObject)
    def __get__(self, this, cls):

        self.__init()

        if not self.__is_static and this.__javaobject__ is None:
            raise TypeError("Field is not static.")

        if self.__thandler.javaType in (EJavaType.VOID, EJavaType.ARRAY):
            raise TypeError("Unknown field type {}.".format(
                            util.to_jep_jtype(self.__thandler.javaType)))

        if self.__is_static:
            return self.__thandler.getStatic(self.__jfield, this.__javaclass__)
        else:
            return self.__thandler.getInstance(self.__jfield, this.__javaobject__)

    @annotate(this=PyJObject)
    def __set__(self, this, value):

        from ..__config__ import config

        self.__init()

        if not self.__is_static and this.__javaobject__ is None:
            raise TypeError("Field is not static.")

        if self.__thandler.javaType in (EJavaType.VOID, EJavaType.ARRAY):
            raise TypeError("Unknown field type {}.".format(
                            util.to_jep_jtype(self.__thandler.javaType)))

        from . import _typehandler as self__thandler

      #if self.__thandler.match(value) <= EMatchType.EXPLICIT: # <AK> added
        if self__thandler.match(value, self.__jfield.getType()) <= EMatchType.EXPLICIT: # <AK> added
            msg = {EJavaType.SHORT:  "int",
                   EJavaType.FLOAT:  "float (jfloat)",
                   EJavaType.DOUBLE: "float (jdouble)",
                   EJavaType.STRING: "string",
                   EJavaType.OBJECT: "object",
                   EJavaType.CLASS:  "class"}
            raise TypeError("Expected {}.".format(msg.get(self.__thandler.javaType,
                                                          self.__thandler.getClassName())))
        if config.getboolean("WITH_VALID", False) and not self.__thandler.valid(value):
            raise ValueError("Assigned value is not valid for required field type.")

        if self.__is_static:
            self.__thandler.setStatic(self.__jfield, this.__javaclass__, value)
        else:
            self.__thandler.setInstance(self.__jfield, this.__javaobject__, value)


@public
class PyConstJField(PyJField):

    __slots__ = ()

    @annotate(this=PyJObject)
    def __delete__(self, this):

        raise AttributeError("Field is undeletable")
