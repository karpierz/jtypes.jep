# Copyright (c) 2014-2017 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import, print_function

import unittest
import sys
import os
import logging

from . import test_dir

test_java = os.path.join(test_dir, "java")
test_jlib = os.path.join(test_dir, "lib")


def test_suite(names=None, omit=("test_jdbc",)):

    from . import __name__ as pkg_name
    from . import __path__ as pkg_path
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


def runTest():

    print("Running testsuite", "\n", file=sys.stderr)

    from jt.jep._jep._jvm import start_jvm, stop_jvm
    from jt.jep           import setupImporter
    start_jvm(path=r"C:/Program Files/Java/jre1.8.0_152/bin/client/jvm.dll",
              options=["-Djava.class.path={}".format(os.pathsep.join(
                       [os.path.join(test_java, "classes"),
                        os.path.join(test_jlib, "sqlitejdbc-v056.jar")])),
                       "-ea", "-Xms64M", "-Xmx256M"])
    setupImporter(None)
    try:
        tests = test_suite(sys.argv[1:] or None)
        result = unittest.TextTestRunner(verbosity=2).run(tests)
    #except SystemExit:
    #    pass
    finally:
        stop_jvm()

    sys.exit(0 if result.wasSuccessful() else 1)


def main():

    # logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.DEBUG)
    runTest()


main()
