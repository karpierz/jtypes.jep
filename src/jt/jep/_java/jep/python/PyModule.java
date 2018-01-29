//
//
//

package jep.python;

import jep.Jep;
import jep.JepException;
import org.python.core.PyException;

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
        this.isValid();
        try
        {
            PyModule module = new PyModule(this.tstate,
                                           this.new_module(this.tstate, this.obj, name),
                                           this.jep);
            this.jep.trackObject(module);
            return module;
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public Object getValue(String name) throws JepException
    {
        this.isValid();
        try
        {
            return this.get_object(this.tstate, this.obj, name);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }
}
