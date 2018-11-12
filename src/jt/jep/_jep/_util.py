# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from ...jvm.lib.compat import *
from ...jvm.lib import annotate

from ._constants import EJavaType


@annotate(EJavaType, jclass='jvm.JClass')
def get_jtype(jclass):

    # Given the Class object, return the const ID, -1 on error or NULL.

    if jclass is None: return -1

    with jclass.jvm as (jvm, jenv):
        if jenv.IsAssignableFrom(jclass.handle, jvm.Object.Class):
            if   jenv.IsSameObject(jclass.handle, jvm.String.Class):    return EJavaType.STRING
            elif jclass.isArray():                                      return EJavaType.ARRAY
            elif jenv.IsAssignableFrom(jclass.handle, jvm.Class.Class): return EJavaType.CLASS
            # TODO: contemplate adding List and jep.NDArray check in here
            # ok it's not a string, array, or class, so let's call it object
            else:                                                       return EJavaType.OBJECT
        elif jenv.IsSameObject(jclass.handle, jvm.Void.TYPE):           return EJavaType.VOID
        elif jenv.IsSameObject(jclass.handle, jvm.Boolean.TYPE):        return EJavaType.BOOLEAN
        elif jenv.IsSameObject(jclass.handle, jvm.Character.TYPE):      return EJavaType.CHAR
        elif jenv.IsSameObject(jclass.handle, jvm.Byte.TYPE):           return EJavaType.BYTE
        elif jenv.IsSameObject(jclass.handle, jvm.Short.TYPE):          return EJavaType.SHORT
        elif jenv.IsSameObject(jclass.handle, jvm.Integer.TYPE):        return EJavaType.INT
        elif jenv.IsSameObject(jclass.handle, jvm.Long.TYPE):           return EJavaType.LONG
        elif jenv.IsSameObject(jclass.handle, jvm.Float.TYPE):          return EJavaType.FLOAT
        elif jenv.IsSameObject(jclass.handle, jvm.Double.TYPE):         return EJavaType.DOUBLE
        else:                                                           return -1


to_jep_jtype = {
    EJavaType.BOOLEAN: 0,  # JBOOLEAN_ID
    EJavaType.INT:     1,  # JINT_ID
    EJavaType.LONG:    2,  # JLONG_ID
    EJavaType.OBJECT:  3,  # JOBJECT_ID
    EJavaType.STRING:  4,  # JSTRING_ID
    EJavaType.VOID:    5,  # JVOID_ID
    EJavaType.DOUBLE:  6,  # JDOUBLE_ID
    EJavaType.SHORT:   7,  # JSHORT_ID
    EJavaType.FLOAT:   8,  # JFLOAT_ID
    EJavaType.ARRAY:   9,  # JARRAY_ID
    EJavaType.CHAR:   10,  # JCHAR_ID
    EJavaType.BYTE:   11,  # JBYTE_ID
    EJavaType.CLASS:  12,  # JCLASS_ID
    }

from_jep_jtype = {v: k for k, v in to_jep_jtype.items()}
