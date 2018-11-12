// Copyright (c) 2014-2018 Adam Karpierz
// Licensed under the zlib/libpng License
// http://opensource.org/licenses/zlib

package jep;

import java.util.Set;

import org.python.util.PythonInterpreter;
import org.python.util.ClassEnquirer;

public class JepConfig extends PythonInterpreter.Config
{
    // A configuration object for constructing a Jep instance, corresponding
    // to the configuration of the particular Python sub-interpreter.
    // This class is intended to make constructing Jep instances easier while
    // maintaining compatible APIs between releases.

    public JepConfig setInteractive(boolean interactive)
    {
        super.setInteractive(interactive);
        return this;
    }

    public JepConfig setIncludePath(String includePath)
    {
        super.setIncludePath(includePath);
        return this;
    }

    public JepConfig addIncludePaths(String... includePaths)
    {
        super.addIncludePaths(includePaths);
        return this;
    }

    public JepConfig setClassLoader(ClassLoader classLoader)
    {
        super.setClassLoader(classLoader);
        return this;
    }

    public JepConfig setClassEnquirer(ClassEnquirer classEnquirer)
    {
        super.setClassEnquirer(classEnquirer);
        return this;
    }

    public JepConfig setRedirectOutputStreams(boolean redirectOutputStreams)
    {
        super.setRedirectOutputStreams(redirectOutputStreams);
        return this;
    }

    public JepConfig setSharedModules(Set<String> sharedModules)
    {
        super.setSharedModules(sharedModules);
        return this;
    }

    public JepConfig addSharedModules(String... sharedModule)
    {
        super.addSharedModules(sharedModule);
        return this;
    }

    public Jep createJep() throws JepException
    {
        // Creates a new Jep instance and its associated sub-interpreter with
        // this JepConfig.

        return new Jep(this);
    }
}
