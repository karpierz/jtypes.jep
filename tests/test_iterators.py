from __future__ import absolute_import
import unittest
import sys
import os
from .jep_pipe import jep_pipe                  #<AK> was: from jep_pipe


class TestIterators(unittest.TestCase):

    def test_iteration(self):
        from java.util import ArrayList
        x = ArrayList()
        x.add("abc")
        x.add("adef")
        x.add("ahi")
        itr = x.iterator()
        for i in x:
            self.assertIn("a", i)

    @unittest.skip("jt.jep: not all things are implemented")
    @unittest.skipIf(sys.platform.startswith("win"), "subprocess complications on Windows")
    def test_iter_itr_crash(self):
        currd = os.path.dirname(os.path.abspath(__file__))
        with jep_pipe(["jep", os.path.join(currd,"subprocess","iter_itr_crash.py")]) as p:
            self.assertEqual(next(p), "success: no crash\n")
