# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

### !!! ###

from ....jvm.lib.compat import long, str as unicode
from ....jvm.lib import annotate
from ....jvm.lib import public

@annotate(int, paramType='jvm.JClass')
def match(arg, paramType):

    from .._constants import EJavaType
    from .._jclass    import PyJClass
    from .._jobject   import PyJObject
    from .._jarray    import PyJArray
    from ..           import _util as util

    # Determines how well a parameter matches the expected type.
    # For example a python integer can be passed to java as a bool, int, long,
    # or java.lang.Integer. A bool is not very descriptive so it would return
    # a much lower value than an int. A return value of 0 indicates there is
    # no match, for example a python int cannot be used as a java.util.List.
    # Larger return values indicate a better match.

    param_jtype = util.get_jtype(paramType)

    if param_jtype == EJavaType.BOOLEAN:

        if isinstance(arg, bool):
            return 8
        elif isinstance(arg, (long, int)):
            return 5
        elif isinstance(arg, (list, tuple, dict)):
            return 1
        return 0 # no match

    elif param_jtype == EJavaType.CHAR:

        if isinstance(arg, (str, unicode)):
            if len(arg) == 1:
                return 2
        return 0 # no match

    elif param_jtype == EJavaType.BYTE:

        if isinstance(arg, bool):
            return 7
        elif isinstance(arg, (long, int)):
            return 6
        return 0 # no match

    elif param_jtype == EJavaType.SHORT:

        if isinstance(arg, bool):
            return 6
        elif isinstance(arg, (long, int)):
            return 7
        return 0 # no match

    elif param_jtype == EJavaType.INT:

        if isinstance(arg, bool):
            return 5
        elif isinstance(arg, long):
            return 10
        elif isinstance(arg, int):
            return 11
        return 0 # no match

    elif param_jtype == EJavaType.LONG:

        if isinstance(arg, bool):
            return 4
        elif isinstance(arg, long):
            return 11
        elif isinstance(arg, int):
            return 10
        return 0 # no match

    elif param_jtype == EJavaType.FLOAT:

        if isinstance(arg, bool):
            return 0 # no match
        elif isinstance(arg, (long, int)):
            return 8
        elif isinstance(arg, float):
            return 5
        return 0 # no match

    elif param_jtype == EJavaType.DOUBLE:

        if isinstance(arg, bool):
            return 0 # no match
        elif isinstance(arg, (long, int)):
            return 9
        elif isinstance(arg, float):
            return 6
        return 0 # no match

    elif param_jtype == EJavaType.STRING:

        if arg is None:
            return 2
        elif isinstance(arg, (str, unicode)):
            return 3
        return 0 # no match

    elif param_jtype == EJavaType.OBJECT:

        if arg is None:
            return 4
        elif isinstance(arg, bool):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, jvm.Boolean.Class):
                    return 3
                elif jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 1
                elif jenv.IsAssignableFrom(jvm.Boolean.Class, paramType.handle):
                    return 2
        elif isinstance(arg, long):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, jvm.Long.Class):
                    return 4
                elif jenv.IsSameObject(paramType.handle, jvm.Integer.Class):
                    return 3
                elif jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 1
                elif jenv.IsAssignableFrom(jvm.Long.Class, paramType.handle):
                    return 2
        elif isinstance(arg, int):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, jvm.Integer.Class):
                    return 4
                elif jenv.IsSameObject(paramType.handle, jvm.Long.Class):
                    return 3
                elif jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 1
                elif jenv.IsAssignableFrom(jvm.Integer.Class, paramType.handle):
                    return 2
        elif isinstance(arg, float):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, jvm.Double.Class):
                    return 4
                elif jenv.IsSameObject(paramType.handle, jvm.Float.Class):
                    return 3
                elif jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 1
                elif jenv.IsAssignableFrom(jvm.Double.Class, paramType.handle):
                    return 2
        elif isinstance(arg, (str, unicode)):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsAssignableFrom(jvm.String.Class, paramType.handle):
                    return 1
        elif isinstance(arg, PyJArray):
            return 1
        elif isinstance(arg, PyJClass):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsAssignableFrom(jvm.Class.Class, paramType.handle):
                    return 1
        elif isinstance(arg, PyJObject):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, arg.__javaclass__.handle):
                    return 3
                elif jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 1
                elif jenv.IsAssignableFrom(arg.__javaclass__.handle, paramType.handle):
                    return 2
        elif isinstance(arg, list):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 2
                elif jenv.IsSameObject(paramType.handle, paramType.jvm.java_util.ArrayListClass):
                    return 4
                elif jenv.IsAssignableFrom(paramType.jvm.java_util.ListClass, paramType.handle):
                    return 3
        elif isinstance(arg, tuple):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 2
                elif jenv.IsAssignableFrom(paramType.jvm.java_util.ListClass, paramType.handle):
                    return 3
        elif isinstance(arg, dict):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsSameObject(paramType.handle, jvm.Object.Class):
                    return 2
                elif jenv.IsAssignableFrom(paramType.jvm.java_util.MapClass, paramType.handle):
                    return 3
        return 0 # no match

    elif param_jtype == EJavaType.ARRAY:

        if arg is None:
            return 3
        elif isinstance(arg, PyJArray):
            with paramType.jvm as (jvm, jenv):
                if jenv.IsAssignableFrom(arg.__javaclass__.handle, paramType.handle):
                    return 2
        return 0 # no match

    elif param_jtype == EJavaType.CLASS:

        if arg is None:
            return 1
        elif isinstance(arg, PyJClass):
            return 2
        return 0 # no match

    elif param_jtype == EJavaType.VOID:

        return 0 # no match

    else:
        return 0 # no match

### !!! ###
