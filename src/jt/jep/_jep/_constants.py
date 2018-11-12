# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib import public
from ...jvm.lib import enumc
from ...jvm     import EJavaType
from ...jvm     import EJavaModifiers

public(EJavaType      = EJavaType)
public(EJavaModifiers = EJavaModifiers)

public(
EMatchType = enumc(
    NONE     =   0,
    EXPLICIT =   1,
    IMPLICIT =  10,
    PERFECT  = 100,
))
