from __future__ import absolute_import
import unittest
import sys
from .jep_pipe import jep_pipe                # <AK> was: from jep_pipe
from .jep_pipe import build_java_process_cmd  # <AK> was: from jep_pipe


class TestInvokes(unittest.TestCase):

    @unittest.skipIf(sys.platform.startswith("win"), "subprocess complications on Windows")
    def test_inits(self):
        jep_pipe(build_java_process_cmd('jep.test.TestInvoke'))
