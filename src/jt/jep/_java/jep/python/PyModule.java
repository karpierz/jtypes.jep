// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep.python;

import jep.Jep;
import jep.JepException;
import org.python.core.PyException;

@Deprecated
public class PyModule extends PyObject
{
    public PyModule(long tstate, long obj, Jep jep) throws JepException, PyException
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

    public PyModule createModule(String name) throws JepException
    {
        super.checkValid();
        try
        {
            long module_obj = super.import_module(super.interp.tstate, super.pyobj, name);
            PyModule module = new PyModule(super.interp.tstate,
                                           module_obj,
                                           (Jep) super.interp);
            super.interp.memoryManager.addReference(module);
            return module;
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public Object getValue(String name) throws JepException
    {
        super.checkValid();
        try
        {
            return super.get_object(super.interp.tstate, super.pyobj, name, Object.class);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }
}
