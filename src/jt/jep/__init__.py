# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from . import __config__ ; del __config__
from .__about__ import * ; del __about__

VERSION = __VERSION__  = __version__

try:
    from ._jep import *
except ImportError:
    raise ImportError("Jep is not supported in standalone Python, it must be embedded in Java.")
from .java_import_hook import *
from .shared_modules_hook import *
