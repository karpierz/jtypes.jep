from jt.jvm.java.class2py import *

header = \
"""\
# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

"""

if __name__ == "__main__":
    import sys
    class2py(sys.argv[1], header=header)
