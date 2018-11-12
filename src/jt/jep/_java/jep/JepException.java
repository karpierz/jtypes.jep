// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep;

import org.python.core.PyException;

public class JepException extends PyException
{
    private static final long serialVersionUID = 1L;

    public JepException()
    {
        super();
    }

    public JepException(String message)
    {
        super(message);
    }

    public JepException(String message, Throwable cause)
    {
        super(message, cause);
    }

    public JepException(Throwable cause)
    {
        super(cause);
    }

    // --------------- internal use only. --------------- //

    protected JepException(String message, long python_type)
    {
        super(message, python_type);
    }
}
