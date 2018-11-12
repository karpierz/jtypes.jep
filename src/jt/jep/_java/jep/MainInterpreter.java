// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep;

import org.python.util.PythonInterpreter;
import org.python.core.PyException;

public final class MainInterpreter extends PythonInterpreter.Python
{
    private static MainInterpreter instance = null;

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

    protected static synchronized MainInterpreter getMainInterpreter() throws Error
    {
        if ( instance == null )
           instance = new MainInterpreter(PythonInterpreter.Python.getInstance());
        return instance;
    }

    private MainInterpreter(PythonInterpreter.Python interp)
    {
        super(interp);
    }

    public void sharedImport(String module) throws JepException
    {
        try
        {
            super.sharedImport(module);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }
}
