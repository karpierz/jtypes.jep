# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import

import types
import traceback

from ...jvm.lib.compat import *
from ...jvm.lib.compat import PY3
from ...jvm.lib import annotate
from ...jvm.lib import public
from ...jvm.lib import cached

from ._jobject import PyJObject
from ._jobject import PyJType
from ._jmethod import PyJConstructor
from ._jmethod import PyJMultiMethod


@public
class PyJClass(PyJObject):

    """jclass"""

    # "jep.PyJClass" # tp_name

    # A PyJClass is a PyJObject with a __call__ method attached,
    # where the call method can invoke the Java object's constructors
    # (either a PyJConstructor or PyJMultiMethod with many PyJConstructors).

    @annotate(jclass='jt.jvm.JClass')
    def __new__(cls, jclass):

        self = super(PyJClass, cls).__new__(cls, None, jclass)
        self.__javaobject__ = None    # jt.jvm.JObject
        self.__javaclass__  = jclass  # jt.jvm.JClass
        self.__constructor  = None # PyJConstructor | PyJMultiMethod
        self.__init()
        return self

    def __init(self):

        # Attempt to add a Java class's public inner classes as attributes
        # to the PyJClass since lots of people code with public enum.
        # Note this will not allow the inner class to be imported separately,
        # it must be accessed through the enclosing class.

        try:
            inner_classes = PyJType._process_inner_classes(self.__javaclass__)
            for inner_cname, inner_class in inner_classes.items():
                try:
                    self._attr_dict[inner_cname] = inner_class
                except:
                    print("Error adding inner class {}".format(inner_cname))
        except:
            # let's just print the error to stderr and continue on without
            # inner class support, it's not the end of the world
            traceback.print_exc()

    @cached
    def __init_constructors(self):

        # Initialize the constructors field of a PyJClass.

        py_callable = None

        constructors = PyJType._process_constructors(self.__javaclass__)
        for i, constructor in enumerate(constructors):
            if i == 0:
                py_callable = constructor
            elif i == 1:
                py_callable = PyJMultiMethod(py_callable, constructor)
            else:
                py_callable._add_overload(constructor)

        self.__constructor = py_callable

    def __call__(self, *args, **kwargs):

        # Call constructor as a method and return PyJObject.

        from ._exceptions import TypeError

        self.__init_constructors()

        if self.__constructor is None:
            raise TypeError("No public constructor")

        # Bind the constructor to the jclass so that the jclass
        # will be the first arg when constructor is called.

        bound_constructor = (types.MethodType(self.__constructor, self) if PY3 else
                             types.MethodType(self.__constructor, self, type(self)))
        return bound_constructor(*args, **kwargs)
