// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep;

import org.python.util.PythonInterpreter;

public class PyConfig extends PythonInterpreter.Options
{
    // A configuration object for setting Python pre-initialization parameters.

    public PyConfig setNoSiteFlag(int noSiteFlag)
    {
        super.setNoSiteFlag(noSiteFlag);
        return this;
    }

    public PyConfig setNoUserSiteDirectory(int noUserSiteDirectory)
    {
        super.setNoUserSiteDirectory(noUserSiteDirectory);
        return this;
    }

    public PyConfig setIgnoreEnvironmentFlag(int ignoreEnvironmentFlag)
    {
        super.setIgnoreEnvironmentFlag(ignoreEnvironmentFlag);
        return this;
    }

    public PyConfig setVerboseFlag(int verboseFlag)
    {
        super.setVerboseFlag(verboseFlag);
        return this;
    }

    public PyConfig setOptimizeFlag(int optimizeFlag)
    {
        super.setOptimizeFlag(optimizeFlag);
        return this;
    }

    public PyConfig setDontWriteBytecodeFlag(int dontWriteBytecodeFlag)
    {
        super.setDontWriteBytecodeFlag(dontWriteBytecodeFlag);
        return this;
    }

    public PyConfig setHashRandomizationFlag(int hashRandomizationFlag)
    {
        super.setHashRandomizationFlag(hashRandomizationFlag);
        return this;
    }

    public PyConfig setPythonHome(String pythonHome)
    {
        super.setPythonHome(pythonHome);
        return this;
    }
}
