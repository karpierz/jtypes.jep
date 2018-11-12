# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import

import sys

from ..jvm.lib import public

from . import _jep
from . import _jpackage


@public
class JepJavaImporter(object):

    def __init__(self, class_enquirer=None):

        self.classEnquirer = (class_enquirer if class_enquirer else
                              _jep.forName("org.python.util.ClassListEnquirer").getInstance())
                           #_jep.findClass("org.python.util.ClassListEnquirer").getInstance()) #!!!

    def find_module(self, fullname, path=None):

        return self if self.classEnquirer.isJavaPackage(fullname) else None

    def load_module(self, fullname):

        if fullname in sys.modules:
            return sys.modules[fullname]

        Package = _jpackage.Package

        module = Package(fullname)
        module.__dict__.update({
            "__loader__":  self,
            "__path__":    [],
            "__file__":    "<java>",
            "__package__": None,
            "__classEnquirer__": self.classEnquirer,
        })
        sys.modules[fullname] = module
        return module


@public
def setupImporter(class_enquirer):

    if any(isinstance(importer, JepJavaImporter) for importer in sys.meta_path):
        return
    sys.meta_path.insert(0, JepJavaImporter(class_enquirer))


def unregister():  # <AK> added

    for importer in sys.meta_path[:]:
        if isinstance(importer, JepJavaImporter):
            sys.meta_path.remove(importer)
