// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Map;

import org.python.util.PythonInterpreter;
import org.python.util.ClassEnquirer;
import org.python.core.PyException;

public class Jep extends PythonInterpreter
{
    @Deprecated
    public static void setInitParams(PyConfig config) throws JepException
    {
        try
        {
            PythonInterpreter.Python.setInitOptions((PythonInterpreter.Options) config);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public static void setSharedModulesArgv(String... argv) throws JepException
    {
        try
        {
            PythonInterpreter.Python.setSharedModulesArgv(argv);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ----------------------------- internals ------------------------------ //

    private static Jep Jep_JepConfig(JepConfig config, boolean useSubInterpreter)
        throws JepException
    {
        try
        {
            return new Jep(new PythonInterpreter((PythonInterpreter.Config) config,
                                                 useSubInterpreter));
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    private Jep(PythonInterpreter interp)
    {
        super(interp);
    }

    // ---------------------------- constructors ---------------------------- //

    public Jep() throws JepException
    {
        this(new JepConfig());
    }

    @Deprecated
    public Jep(boolean interactive) throws JepException
    {
        this(interactive, null, null, null);
    }

    @Deprecated
    public Jep(boolean interactive, String includePath) throws JepException
    {
        this(interactive, includePath, null, null);
    }

    @Deprecated
    public Jep(boolean interactive, String includePath, ClassLoader classLoader)
        throws JepException
    {
        this(interactive, includePath, classLoader, null);
    }

    @Deprecated
    public Jep(boolean interactive, String includePath, ClassLoader classLoader,
               ClassEnquirer classEnquirer) throws JepException
    {
        this(new JepConfig().setInteractive(interactive)
                            .setIncludePath(includePath)
                            .setClassLoader(classLoader)
                            .setClassEnquirer(classEnquirer));
    }

    public Jep(JepConfig config) throws JepException
    {
        this(config, true);
    }

    protected Jep(JepConfig config, boolean useSubInterpreter) throws JepException
    {
        this(Jep_JepConfig(config, useSubInterpreter));
    }

    @Override
    public synchronized void close() throws JepException
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

    // ------------------------------ settings ------------------------------ //

    public void setClassLoader(ClassLoader classLoader) throws JepException
    {
        try
        {
            super.setClassLoader(classLoader);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ----------------------------- run things ----------------------------- //

    public void runScript(String script) throws JepException
    {
        try
        {
            super.execfile(script);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public void runScript(String script, ClassLoader classLoader) throws JepException
    {
        try
        {
            super.execfile(script, classLoader);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public Boolean eval(String str) throws JepException
    {
        try
        {
            return super.eval(str) != null;
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public Object invoke(String name, Object... args) throws JepException
    {
        try
        {
            return super.invoke(name, args);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public Object invoke(String name, Map<String, Object> kwargs) throws JepException
    {
        try
        {
            return super.invoke(name, kwargs);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public Object invoke(String name, Object[] args, Map<String, Object> kwargs)
        throws JepException
    {
        try
        {
            return super.invoke(name, args, kwargs);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public jep.python.PyModule createModule(String name) throws JepException
    {
        try
        {
            long module_obj = super.import_module(super.tstate, name);
            return new jep.python.PyModule(super.tstate, module_obj, this);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ----------------------------- get values ----------------------------- //

    public Object getValue(String name) throws JepException
    {
        try
        {
            return super.get(name);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public byte[] getValue_bytearray(String name) throws JepException
    {
        try
        {
            return super.getByteArray(name);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    @Deprecated
    public float[] getValue_floatarray(String name) throws JepException
    {
        try
        {
            byte[] barr = super.getByteArray(name);
            ByteBuffer bbuf = ByteBuffer.wrap(barr).order(ByteOrder.nativeOrder());
            return bbuf.asFloatBuffer().array();
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    // ----------------------------- set values ----------------------------- //

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

    // ----------------------------- set arrays ----------------------------- //

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
}
