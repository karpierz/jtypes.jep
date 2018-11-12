# Copyright (c) 2014-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import, division

import numbers

from ...jvm.lib.compat import *
from ...jvm.lib.compat import PY2
from ...jvm.lib import py2compatible
from ...jvm.lib import annotate, Union
from ...jvm.lib import public

from ._jobject import PyJObject


@public
@py2compatible
class PyJNumber(PyJObject):

    """jnumber"""

    # "jep.PyJNumber" # tp_name

    # A PyJNumber is a PyJObject with some extra methods attached to meet
    # the Python Number protocol/interface.  It should only be used where the
    # underlying jobject of the PyJObject is an implementation of java.lang.Number.

    def __add__(self, other):

        return _java_number_to_python(self) + _to_python_number(other)

    def __sub__(self, other):

        return _java_number_to_python(self) - _to_python_number(other)

    def __mul__(self, other):

        return _java_number_to_python(self) * _to_python_number(other)

    if PY2:
        def __div__(self, other):

            self_num, other_num = _java_number_to_python(self), _to_python_number(other)
            if (isinstance(self_num,  numbers.Integral) and
                isinstance(other_num, numbers.Integral)):
                return self_num // other_num
            else:
                return self_num / other_num

    def __mod__(self, other):

        return _java_number_to_python(self) % _to_python_number(other)

    def __divmod__(self, other):

        return divmod(_java_number_to_python(self), _to_python_number(other))

    def __pow__(self, other, modulo=None):

        return pow(_java_number_to_python(self), _to_python_number(other),
                   _to_python_number(modulo) if modulo is not None else None)

    def __neg__(self):

        return -_java_number_to_python(self)

    def __pos__(self):

        return +_java_number_to_python(self)

    def __abs__(self):

        return abs(_java_number_to_python(self))

    def __bool__(self):

        return not not _java_number_to_python(self)

    def __floordiv__(self, other):

        return _java_number_to_python(self) // _to_python_number(other)

    def __truediv__(self, other):

        return _java_number_to_python(self) / _to_python_number(other)

    def __index__(self):

        idx = _java_number_to_python(self)

        if not isinstance(idx, (int, long)):
            raise TypeError("list indices must be integers, not {}".format(
                            type(idx).__name__))
        return int(idx)

    def __int__(self):

        return _java_number_to_python_integral(self)

    if PY2:
        def __long__(self):

            return long(_java_number_to_python_integral(self))

    def __float__(self):

        return _java_number_to_python_float(self)

    def __eq__(self, other):

        return _java_number_to_python(self) == _to_python_number(other)

    def __ne__(self, other):

        return _java_number_to_python(self) != _to_python_number(other)

    def __lt__(self, other):

        return _java_number_to_python(self) < _to_python_number(other)

    def __gt__(self, other):

        return _java_number_to_python(self) > _to_python_number(other)

    def __le__(self, other):

        return _java_number_to_python(self) <= _to_python_number(other)

    def __ge__(self, other):

        return _java_number_to_python(self) >= _to_python_number(other)

    def __hash__(self):

        if isinstance(self, PyJNumber):
            try:
                self_num = _java_number_to_python(self)
            except:
                return -1
            else:
                return hash(self_num)
        else:
            return hash(self)


@annotate(Union[int, long, float, numbers.Number])
def _to_python_number(var):

    if isinstance(var, PyJNumber):
        return _java_number_to_python(var)
    elif isinstance(var, numbers.Number):
        return var
    else:
        return NotImplemented


@annotate(Union[int, long, float], jnumber=PyJNumber)
def _java_number_to_python(jnumber):

    jnumber_jobj = jnumber.__javaobject__

    with jnumber_jobj.jvm as (jvm, jenv):
        is_integer  = (jenv.IsInstanceOf(jnumber_jobj.handle, jvm.Byte.Class)  or
                       jenv.IsInstanceOf(jnumber_jobj.handle, jvm.Short.Class) or
                       jenv.IsInstanceOf(jnumber_jobj.handle, jvm.Integer.Class))
        is_integral = (is_integer or
                       jenv.IsInstanceOf(jnumber_jobj.handle, jvm.Long.Class))

    if PY2 and is_integer:
        return jnumber_jobj.intValue()
    elif is_integral:
        return jnumber_jobj.longValue()
    else:
        return jnumber_jobj.doubleValue()


@annotate(Union[int, long], jnumber=PyJNumber)
def _java_number_to_python_integral(jnumber):

    jnumber_jobj = jnumber.__javaobject__

    with jnumber_jobj.jvm as (jvm, jenv):
        is_integer = (PY2 and
                      (jenv.IsInstanceOf(jnumber_jobj.handle, jvm.Byte.Class)  or
                       jenv.IsInstanceOf(jnumber_jobj.handle, jvm.Short.Class) or
                       jenv.IsInstanceOf(jnumber_jobj.handle, jvm.Integer.Class)))
    if is_integer:
        return jnumber_jobj.intValue()
    else:
        return jnumber_jobj.longValue()


@annotate(float, jnumber=PyJNumber)
def _java_number_to_python_float(jnumber):

    jnumber_jobj = jnumber.__javaobject__

    return jnumber_jobj.doubleValue()
