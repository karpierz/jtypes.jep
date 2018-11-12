from __future__ import absolute_import
import unittest
import sys
from .jep_pipe import jep_pipe                # <AK> was: from jep_pipe
from .jep_pipe import build_java_process_cmd  # <AK> was: from jep_pipe


@unittest.skipIf(sys.platform.startswith("win"), "subprocess complications on Windows")
class TestGetValue(unittest.TestCase):

    def test_get_collection_boxing(self):
        jep_pipe(build_java_process_cmd('jep.test.TestGetCollectionBoxing'))

    def test_get_bytearray(self):
        jep_pipe(build_java_process_cmd('jep.test.TestGetByteArray'))

    def test_get_temp_value(self):
        jep_pipe(build_java_process_cmd('jep.test.TestGetTempValue'))

    def test_get_with_class(self):
        jep_pipe(build_java_process_cmd('jep.test.TestGetWithClass'))

    def test_get_jpyobject(self):
        jep_pipe(build_java_process_cmd('jep.test.TestGetJPyObject'))
