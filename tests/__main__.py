# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import, print_function

import unittest
import sys
import os
import importlib
import logging

from . import test_dir

test_java = os.path.join(test_dir, "java")
test_jlib = os.path.join(test_dir, "lib")


def test_suite(names=None, omit=("run", "runtests", "test_jdbc")):

    from .python import __name__ as pkg_name
    from .python import __path__ as pkg_path
    import unittest
    import pkgutil
    if names is None:
        names = [name for _, name, _ in pkgutil.iter_modules(pkg_path)
                 if name != "__main__" and name not in omit]
    names = [".".join((pkg_name, name)) for name in names]
    tests = unittest.defaultTestLoader.loadTestsFromNames(names)
    return tests


# embedding does not setup argv
sys.argv = [""]


def main():

    sys.modules["jep"]                     = importlib.import_module("jt.jep")
    sys.modules["jep.__about__"]           = importlib.import_module("jt.jep.__about__")
    sys.modules["jep.console"]             = importlib.import_module("jt.jep.console")
    sys.modules["jep.java_import_hook"]    = importlib.import_module("jt.jep.java_import_hook")
    sys.modules["jep.redirect_streams"]    = importlib.import_module("jt.jep.redirect_streams")
    sys.modules["jep.shared_modules_hook"] = importlib.import_module("jt.jep.shared_modules_hook")
    sys.modules["jep.jdbc"]                = importlib.import_module("jt.jep.jdbc")
   #sys.modules["jep.version"]             = importlib.import_module("jt.jep.version")
    sys.modules["jep._jep"]                = importlib.import_module("jt.jep._jep")

    print("Running testsuite", "\n", file=sys.stderr)

    from jt.jep._jep._jvm import start_jvm, stop_jvm

    from jep import java_import_hook
    start_jvm(path=r"C:/Program Files/Java/jdk1.8.0_181/jre/bin/server/jvm.dll",
              options=["-Djava.class.path={}".format(os.pathsep.join(
                       [os.path.join(test_java, "classes"),
                        os.path.join(test_jlib, "sqlitejdbc-v056.jar")])),
                       "-ea", "-Xms64M", "-Xmx256M"])
    java_import_hook.setupImporter(None)
    try:
        tests = test_suite(sys.argv[1:] or None)
        result = unittest.TextTestRunner(verbosity=2).run(tests)
    #except SystemExit:
    #    pass
    finally:
        stop_jvm()

    sys.exit(0 if result.wasSuccessful() else 1)


if __name__.rpartition(".")[-1] == "__main__":
    # logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.DEBUG)
    main()
