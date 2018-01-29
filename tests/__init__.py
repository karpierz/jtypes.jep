# Copyright (c) 2014-2017 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import

__all__ = ('top_dir', 'test_dir')

import sys, os, importlib
if sys.version_info.major <= 2:
    sys.modules["unittest"] = importlib.import_module("unittest2")
sys.dont_write_bytecode = True
test_dir = os.path.dirname(os.path.abspath(__file__))
top_dir = os.path.dirname(test_dir)
del sys, os, importlib

__all__ += ('with_performance',)

def with_performance():
    return False #!!!