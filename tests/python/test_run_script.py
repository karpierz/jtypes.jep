from __future__ import absolute_import
import unittest
import os
import os.path

from .jep_pipe import jep_pipe                # <AK> was: from jep_pipe
from .jep_pipe import build_java_process_cmd  # <AK> was: from jep_pipe

# <AK> added and changed appropriate paths for using it
build_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'build')


class TestRunScript(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(build_dir, 'testScript.py'), 'w') as testScript:
            testScript.write("def isGood():\n")
            testScript.write("    return True\n")
        

    def test_compiledScript(self):
        jep_pipe(build_java_process_cmd('jep.test.TestCompiledScript'))


    def tearDown(self):
        if os.path.exists(os.path.join(build_dir, 'testScript.py')):
            os.remove(os.path.join(build_dir, 'testScript.py'))
        if os.path.exists(os.path.join(build_dir, 'testScript.pyc')):
            os.remove(os.path.join(build_dir, 'testScript.pyc'))

