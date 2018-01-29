@echo off
setlocal
pushd "%~dp0"
if not defined JAVA_HOME ( set JAVA_HOME="C:\Program Files\Java\jdk1.8.0_152" )
set javac=%JAVA_HOME%\bin\javac -encoding UTF-8 -g:none -deprecation -Xlint:unchecked ^
    -source 1.7 -target 1.7 -bootclasspath "C:\Program Files\Java\jdk1.7.0_79\jre\lib\rt.jar"
rmdir /Q/S java\classes 2> nul & mkdir java\classes
dir /S/B/O:N ^
    ..\..\jtypes.jvm\src\jt\jvm\java\org\python\*.java ^
    ..\..\jtypes.jvm\src\jt\jvm\java\com\jt\util\*.java ^
    ..\src\jt\jep\_java\jep\*.java ^
    java\*.java 2> nul > build.fil
%javac% -d java/classes -classpath lib/* @build.fil
del /F/Q build.fil
copy /V/Y/B ^
    ..\..\jtypes.jvm\src\jt\jvm\java\com\jt\util\classlist_*.txt java\classes\com\jt\util\ > nul
popd
endlocal
