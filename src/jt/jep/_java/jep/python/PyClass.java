//
//
//

package jep.python;

import jep.Jep;
import jep.JepException;
import org.python.core.PyException;

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
