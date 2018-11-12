# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import

import types

from ..jvm.lib import public

from . import _jep


@public
class Package(types.ModuleType):

    """Lazy load classes not found at runtime.

    Introspecting Java packages is difficult, there is not a good
    way to get a list of all classes for a package. By providing
    a __getattr__ implementation for modules, this class can
    try to find classes manually.

    Based on the ClassEnquirer used, some classes may not appear in dir()
    but will import correctly.
    """

    def __getattr__(self, name):

        try:
            return super(Package, self).__getattribute__(name)
        except AttributeError:
            pkg_names = self.__classEnquirer__.getSubPackages(self.__name__)
            if pkg_names and name in pkg_names:
                full_name = "{}.{}".format(self.__name__, name)
                module = Package(full_name)
                module.__dict__.update({
                    "__loader__":  self.__loader__,
                    "__path__":    [],
                    "__file__":    "<java>",
                    "__package__": None,
                    "__classEnquirer__": self.__classEnquirer__,
                })
                sys.modules[full_name] = module
                return module
            elif name == "__all__":
                return self.__dir__()
            else:
                # assume it is a class and attempt the import
                full_name = "{}.{}".format(self.__name__, name)
                jclass = _jep.forName(full_name)
               #jclass = _jep.findClass(full_name) #!!!
                setattr(self, name, jclass)
                return jclass

    def __dir__(self):

        pkg_names   = self.__classEnquirer__.getSubPackages(self.__name__)
        class_names = self.__classEnquirer__.getClassNames(self.__name__)
        result = []
        if pkg_names:
            result += (pname for pname in pkg_names)
        if class_names:
            result += (cname.split(".")[-1] for cname in class_names)
        return result
