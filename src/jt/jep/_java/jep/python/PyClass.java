// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep.python;

import jep.Jep;
import jep.JepException;
import org.python.core.PyException;

@Deprecated
public class PyClass extends PyObject
{
    public PyClass(long tstate, long obj, Jep jep) throws JepException, PyException
    {
        //try
        //{
            super(tstate, obj, jep);
        //}
        //catch ( PyException exc )
        //{
        //    throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        //}
    }
}
