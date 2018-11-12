@echo off
setlocal
set JAVA8_HOME=C:\Program Files\Java\jdk1.8.0_181
if not defined JAVA_HOME (set JAVA_HOME=%JAVA8_HOME%)
set javac="%JAVA_HOME%"\bin\javac -encoding UTF-8 -g:none -deprecation -Xlint:unchecked ^
    -source 1.8 -target 1.8 -bootclasspath "%JAVA8_HOME%\jre\lib\rt.jar"
set py=C:\Windows\py.exe -3.6 -B
pushd "%~dp0"\src\jt\jep\_java
%javac% ^
    ..\..\..\..\..\jtypes.jvm\src\jt\jvm\java\org\python\*.java ^
    ..\..\..\..\..\jtypes.jvm\src\jt\jvm\java\org\python\core\*.java ^
    ..\..\..\..\..\jtypes.jvm\src\jt\jvm\java\org\python\util\*.java ^
    jep\*.java ^
    jep\reflect\*.java ^
    jep\python\*.java
%py% -m class2py jep\AbstractNDArray.class
%py% -m class2py jep\DirectNDArray.class
%py% -m class2py jep\NDArray.class
%py% -m class2py jep\Jep.class
%py% -m class2py jep\MainInterpreter.class
%py% -m class2py jep\JepException.class
rem %py% -m class2py jep\Run.class
%py% -m class2py jep\reflect\ProxyHandler.class
%py% -m class2py jep\python\PyModule.class
%py% -m class2py jep\python\PyClass.class
%py% -m class2py jep\python\PyObject.class
del /F/Q ^
    ..\..\..\..\..\jtypes.jvm\src\jt\jvm\java\org\python\*.class ^
    ..\..\..\..\..\jtypes.jvm\src\jt\jvm\java\org\python\core\*.class ^
    ..\..\..\..\..\jtypes.jvm\src\jt\jvm\java\org\python\util\*.class ^
    jep\*.class ^
    jep\reflect\*.class ^
    jep\python\*.class
popd
pushd "%~dp0"\tests
rmdir /Q/S java\classes 2> nul & mkdir java\classes
dir /S/B/O:N ^
    ..\..\jtypes.jvm\src\jt\jvm\java\org\python\*.java ^
    ..\src\jt\jep\_java\jep\*.java ^
    java\*.java ^
    2> nul > build.fil
%javac% -d java/classes -classpath lib/* @build.fil
del /F/Q build.fil
mkdir java\classes\com\jt\util
copy /V/Y/B ^
    ..\..\jtypes.jvm\src\jt\jvm\java\com\jt\util\classlist_*.txt ^
    java\classes\com\jt\util\ > nul
popd
endlocal
