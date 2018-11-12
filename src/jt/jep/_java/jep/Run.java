// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep;

import org.python.util.PythonInterpreter;
import org.python.core.PyException;

public class Run extends org.python.util.Run
{
    private Run() { }

    public static void main(String args[]) throws Throwable
    {
        current_class = Run.class;

        try
        {
            org.python.util.Run.main(args);
        }
        catch ( PyException exc )
        {
            throw (JepException) new JepException(exc.getMessage()).initCause(exc);
        }
    }

    public static int run(boolean eventDispatch)
    {
        PythonInterpreter interp = null;
        try
        {
            interp = new Jep(new JepConfig().setInteractive(false)
                                            .setIncludePath("."));
        }
        catch ( Throwable exc )
        {
            exc.printStackTrace();
            return 1;
        }

        return run(eventDispatch, interp);
    }
}
