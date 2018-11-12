// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep.python;

import jep.Jep;
import jep.JepException;
import org.python.util.PythonInterpreter;
import org.python.core.PyException;

public class PyObject extends org.python.core.PyObject
{
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
    }

    @Override
    public void close() throws JepException
    {
        try
        {
            super.close();
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    protected void checkValid() throws JepException
    {
        try
        {
            super.checkValid();
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void isValid() throws JepException
    {
        this.checkValid();
    }

    // ----------- get/set/delete attributes ------------ //

    public Object getAttr(String name) throws JepException
    {
        try
        {
            return super.getAttr(name);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public <T> T getAttr(String name, Class<T> jclass) throws JepException
    {
        try
        {
            return super.getAttr(name, jclass);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void setAttr(String name, Object value) throws JepException
    {
        try
        {
            super.setAttr(name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void delAttr(String name) throws JepException
    {
        try
        {
            super.delAttr(name);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ------------------------- set values ------------------------- //

    @Deprecated
    public void set(String name, boolean value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, char value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, new String(new char[] { value }));
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, byte value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, short value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, int value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, long value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, float value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, double value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, String value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, Object value) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, value);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ------------------------- set arrays ------------------------- //

    @Deprecated
    public void set(String name, boolean[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, char[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, new String(array));
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, byte[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, short[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, int[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, long[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, float[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public void set(String name, double[] array) throws JepException
    {
        try
        {
            super.checkValid();
            this.set_var(super.interp.tstate, super.pyobj, name, array);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    private native void set_var(long tstate, long obj, String name, boolean   value) throws PyException;
    private native void set_var(long tstate, long obj, String name, char      value) throws PyException;
    private native void set_var(long tstate, long obj, String name, byte      value) throws PyException;
    private native void set_var(long tstate, long obj, String name, short     value) throws PyException;
    private native void set_var(long tstate, long obj, String name, int       value) throws PyException;
    private native void set_var(long tstate, long obj, String name, long      value) throws PyException;
    private native void set_var(long tstate, long obj, String name, float     value) throws PyException;
    private native void set_var(long tstate, long obj, String name, double    value) throws PyException;
    private native void set_var(long tstate, long obj, String name, String    value) throws PyException;
    private native void set_var(long tstate, long obj, String name, Object    value) throws PyException;

    private native void set_var(long tstate, long obj, String name, boolean[] array) throws PyException;
    private native void set_var(long tstate, long obj, String name, char[]    array) throws PyException;
    private native void set_var(long tstate, long obj, String name, byte[]    array) throws PyException;
    private native void set_var(long tstate, long obj, String name, short[]   array) throws PyException;
    private native void set_var(long tstate, long obj, String name, int[]     array) throws PyException;
    private native void set_var(long tstate, long obj, String name, long[]    array) throws PyException;
    private native void set_var(long tstate, long obj, String name, float[]   array) throws PyException;
    private native void set_var(long tstate, long obj, String name, double[]  array) throws PyException;

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
