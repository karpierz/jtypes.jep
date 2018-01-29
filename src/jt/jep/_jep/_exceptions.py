# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib.compat import *
from ...jvm.lib import public


@public
class TypeError(builtins.TypeError, RuntimeError):

    """ """

@public
class NoMatchingOverload(builtins.TypeError, RuntimeError):

    """ """
