# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib import public
from ...jvm.lib import enumc

public(
EMatchType = enumc(
    NONE     =   0,
    EXPLICIT =   1,
    IMPLICIT =  10,
    PERFECT  = 100,
))
