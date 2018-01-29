//
//
//

package jep.python;

import jep.Jep;
import jep.JepException;
import org.python.util.PythonInterpreter;
import org.python.core.PyException;

public class PyObject extends org.python.core.PyObject
{
    protected Jep jep = null;  // the interpreter that created this object

    public PyObject(long tstate, long obj, Jep jep) throws JepException, PyException
    {
        //try
        //{
            super((PythonInterpreter) jep, obj);
        //}
        //catch ( PyException exc )
        //{
        //    throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        //}
        this.tstate = tstate;
        this.jep    = jep;
    }

    public void isValid() throws JepException
    {
        try
        {
            super.isValid();
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ------------------------- set values ------------------------- //

    public void set(String name, boolean value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, char value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, byte value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, short value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, int value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, long value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, float value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, double value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, String value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, Object value) throws JepException
    {
        try
        {
            super.set(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ------------------------- set arrays ------------------------- //

    public void set(String name, boolean[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, char[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, byte[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, short[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, int[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, long[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, float[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void set(String name, double[] array) throws JepException
    {
        try
        {
            super.set(name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // --------------------- Internal use only. --------------------- //

    public void incref() throws JepException
    {
        try
        {
            super.incref();
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void decref() throws JepException
    {
        try
        {
            super.decref();
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }
}
