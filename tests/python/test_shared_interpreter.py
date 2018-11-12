from __future__ import absolute_import
import unittest
import sys
from .jep_pipe import jep_pipe                # <AK> was: from jep_pipe
from .jep_pipe import build_java_process_cmd  # <AK> was: from jep_pipe

@unittest.skipIf(sys.platform.startswith("win"), "subprocess complications on Windows")
class TestSharedInterpreter(unittest.TestCase):

    def test_shared_interpreter(self):
        jep_pipe(build_java_process_cmd('jep.test.TestSharedInterpreter'))

