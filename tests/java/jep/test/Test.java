package jep.test;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;  //<AK>: added
import java.util.ArrayList;

import jep.Jep;
import jep.JepConfig;
import jep.JepException;
import org.python.core.PyModule;  //<AK> was: jep.python.PyModule;

/**
 * Test.java
 * 
 * Created: April 2004
 * 
 * @author Mike Johnson
 */
public class Test implements Runnable {

    private Jep jep = null;

    private boolean testEval = false;

    public static ClassLoader restrictedClassLoader = new ClassLoader() {
        @Override
        public Class<?> loadClass(final String name)
                throws ClassNotFoundException {
            if (name.startsWith("java.io.")) {
                throw new ClassNotFoundException("restricted class: " + name);
            }
            return super.loadClass(name);
        }
    };

    public Test() {
    }

    public Test(boolean testEval) {
        this.testEval = testEval;
    }

    @Override
    public void run() {

        for (int i = 0; i < 1; i++) {
            System.out.println("running i: " + i);

            try {
                File pwd = new File(".");

                this.jep = new Jep(new JepConfig().setInteractive(this.testEval)
                        .addIncludePaths(pwd.getAbsolutePath()));
                jep.set("testb", true);
                jep.set("testy", 127);
                jep.set("testi", i);
                jep.set("testl", 123123122112L);
                jep.set("testf", 12312.123123F);
                jep.set("testd", 123.123D);
                jep.set("testc", 't');
                jep.set("test",  "value from java.");
                jep.set("testo", this);
                jep.set("testz", this.getClass());
                jep.set("testn", (String) null);
                jep.set("testn", (Object) null);

                // arrays
                int[] ia = new int[] { 3 };
                double[] da = new double[] { 2.0 };
                String[] sa = new String[] { "0" };

                jep.eval("def manip(li, val):\n\tli[0]=val\n\tli.commit()");
                jep.invoke("manip", ia, 1);
                jep.invoke("manip", da, 1.0);
                jep.invoke("manip", sa, "1");

                System.out.println(ia[0]);
                System.out.println(da[0]);
                System.out.println(sa[0]);

                jep.set("x", da);
                assert ((double[]) jep.getValue("x"))[0] == 1.0;

                boolean[] ab = new boolean[10];
                ab[1] = true;
                jep.set("testab", ab);

                double[] ad = new double[10];
                ad[1] = 1.7976931348623157E308D;
                jep.set("testad", ad);

                //PyModule amod = jep.createModule("amod");
                //amod.set("testab", ab);
                //amod.set("testad", ad);

                if (!this.testEval)
                    jep.runScript("test.py");
                else {
                    BufferedReader buf = new BufferedReader(new FileReader(
                            "test.py"));

                    String line = null;
                    while ((line = buf.readLine()) != null) {
                        if (line.trim().startsWith("#"))
                            continue;

                        System.out.println("Running line: " + line);
                        jep.eval(line);
                    }

                    buf.close();
                }

                jep.invoke("testMethod", true);
                jep.invoke("testMethod", (byte) 211);
                jep.invoke("testMethod", 123);
                jep.invoke("testMethod", 112L);
                jep.invoke("testMethod", 112.2312331F);
                jep.invoke("testMethod", 112.23D);
                jep.invoke("testMethod", 't');

                Object ret = jep
                        .invoke("testMethod", "method called from Java");
                System.out.println("testMethod ret:   " + ret);

                System.out.println("Test get boolean: " + (Boolean) jep.getValue("testb"));
                System.out.println("Test get short:   " + (Integer) jep.getValue("testy"));
                System.out.println("Test get int:     " + ((Integer) jep.getValue("testi")).intValue());
                System.out.println("Test get long:    " + (Long) jep.getValue("testl"));
                System.out.println("Test get float:   " + (Float) jep.getValue("testf"));
                System.out.println("Test get double:  " + (Float) jep.getValue("testd"));
                System.out.println("Test get string:  " + jep.getValue("test"));
                System.out.println("Test get object:  " + jep.getValue("testo"));
                System.out.println("Test get class:   " + (Class) jep.getValue("testz"));
                System.out.println("Test get null:    " + jep.getValue("testn"));

                jep.eval("testmap = {'blah': 'har'}");
                System.out.println("Test get Python object: "
                        + jep.getValue("testmap"));

                System.out.print("get unknown val:  ");

                try {
                    System.out.println(jep.getValue("_asdf"));
                    System.out.println("whoops");
                } catch (JepException e) {
                    System.out.println(e.getMessage());
                }
            } catch (Throwable t) {
                System.out.println("Java caught error:");
                t.printStackTrace();
                break;
            } finally {
                System.out.println("**** close me");
                if (jep != null) {
                    try {
                        jep.close();
                    } catch (JepException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }

    // get the jep used for this class
    public Jep getJep() {
        return this.jep;
    }

    @Override
    public String toString() {
        return "toString(). Thanks for calling Java(tm).";
    }

    public static enum TestEnum { One, Two }
    public TestEnum  getEnum()   { return TestEnum.One; }
    public ArrayList getObject() { return new ArrayList<String>(Arrays.asList("list 0")); }

    public Boolean   getClassBoolean()   { return new Boolean(true);              }
    public Byte      getClassByte()      { return new Byte((byte) 45);            }
    public Short     getClassShort()     { return new Short((short) 31580);       }
    public Integer   getClassInteger()   { return new Integer(-2147483648);       }
    public Long      getClassLong()      { return new Long(9223372036854775807L); }
    public Float     getClassFloat()     { return new Float(3.4028235E38F);       }
    public Double    getClassDouble()    { return new Double(4.9E-324D);          }
    public Character getClassCharacter() { return new Character('x');             }

    public boolean[] getBooleanArray() { return new boolean[] { false, true };               }
    public byte[]    getByteArray()    { return new byte[]    { 45, 45 };                    }
    public short[]   getShortArray()   { return new short[]   { 123, 123 };                  }
    public int[]     getIntArray()     { return new int[]     { 1, 2 };                      }
    public long[]    getLongArray()    { return new long[]    { 6289234456854775807L, 87L }; }
    public float[]   getFloatArray()   { return new float[]   { 123.123F, 123.123F };        }
    public double[]  getDoubleArray()  { return new double[]  { 6.873E-248D, 8.412E48D };    }
    public char[]    getCharArray()    { return new char[]    { 'r', 't' };                  }
    public String[]  getStringArray()  { return new String[]  { "one", "two" };              }
    public Test[]    getObjectArray()  { return new Test[]    { new Test(), new Test() };    }

    public String[][] getStringStringArray() { return new String[][] {
                                                      new String[] { "one", "two" },
                                                      new String[] { "one", "two" } }; }
    public void sendObjectArray(Object p[]) {
        if (p == null)
            throw new NullPointerException("p is null?");
        for (int i = 0; i < p.length; i++)
            System.out.println("                  " + "array[" + i + "] = "
                    + p[i]);
    }

    public void sendIntArray(int p[]) {
        if (p == null)
            throw new NullPointerException("p is null?");
        for (int i = 0; i < p.length; i++)
            System.out.println("                  " + "array[" + i + "] = "
                    + p[i]);
    }

    public void sendMeSomeStuff(String v, ArrayList a) {
        System.out.println("got some stuff:   v = " + v + " and a = " + a);
    }

    public String callback() {
        return "Hey, you called a Java(tm) method!";
    }

    public Object testObjectPassThrough(Object bool) {
        return bool;
    }

    // instance fields

    public boolean booleanField = true;
    public byte    byteField    = 43;
    public short   shortField   = 321;
    public int     intField     = 123;
    public long    longField    = 9223372036854775807L;
    public float   floatField   = 3.4028235E38F;
    public double  doubleField  = 123.123D;
    public char    charField    = 'c';
    public String  stringField  = "a stringField";
    public Class   classField   = this.getClass();

    // static fields

    public static boolean staticBoolean = true;
    public static byte    staticByte    = 125;
    public static short   staticShort   = 321;
    public static int     staticInt     = 123;
    public static long    staticLong    = 9223372036854775807L;
    public static float   staticFloat   = 3.4028235E38F;
    public static double  staticDouble  = 123.123D;
    public static char    staticChar    = 'j';
    public static String  staticString  = "stringField";
    public static Class   staticClass   = Thread.currentThread().getClass();

    // instance methods

    public boolean isBooleanField() { return this.booleanField; }
    public byte    getByteField()   { return this.byteField;    }
    public short   getShortField()  { return this.shortField;   }
    public int     getIntField()    { return this.intField;     }
    public long    getLongField()   { return this.longField;    }
    public float   getFloatField()  { return this.floatField;   }
    public double  getDoubleField() { return this.doubleField;  }
    public char    getCharField()   { return this.charField;    }
    public String  getStringField() { return this.stringField;  }
    public Class   getClassField()  { return this.classField;   }

    public void setBooleanField(boolean value) { this.booleanField = value; }
    public void setByteField(byte       value) { this.byteField    = value; }
    public void setShortField(short     value) { this.shortField   = value; }
    public void setIntField(int         value) { this.intField     = value; }
    public void setLongField(long       value) { this.longField    = value; }
    public void setFloatField(float     value) { this.floatField   = value; }
    public void setDoubleField(double   value) { this.doubleField  = value; }
    public void setCharField(char       value) { this.charField    = value; }
    public void setStringField(String   value) { this.stringField  = value; }
    public void setClassField(Class     value) { this.classField   = value; }

    // static methods

    public static boolean isStaticBoolean() { return Test.staticBoolean; }
    public static byte    getStaticByte()   { return Test.staticByte;    }
    public static short   getStaticShort()  { return Test.staticShort;   }
    public static int     getStaticInt()    { return Test.staticInt;     }
    public static long    getStaticLong()   { return Test.staticLong;    }
    public static float   getStaticFloat()  { return Test.staticFloat;   }
    public static double  getStaticDouble() { return Test.staticDouble;  }
    public static char    getStaticChar()   { return Test.staticChar;    }
    public static String  getStaticString() { return Test.staticString;  }
    public static Object  getStaticObject() { return new Object();       }
    public static Class   getStaticClass()  { return Thread.currentThread().getClass(); }

    public static void setStaticBoolean(boolean value) { Test.staticBoolean = value; }
    public static void setStaticByte(byte       value) { Test.staticByte    = value; }
    public static void setStaticShort(short     value) { Test.staticShort   = value; }
    public static void setStaticInt(int         value) { Test.staticInt     = value; }
    public static void setStaticLong(long       value) { Test.staticLong    = value; }
    public static void setStaticFloat(float     value) { Test.staticFloat   = value; }
    public static void setStaticDouble(double   value) { Test.staticDouble  = value; }
    public static void setStaticChar(char       value) { Test.staticChar    = value; }
    public static void setStaticString(String   value) { Test.staticString  = value; }

    public static void callStaticVoid() { return; }

    public String[] testAllVarArgs(String... args){
        return args;
    }

    public String[] testMixedVarArgs(String regArg1, String regArg2, String... args){
        String[] result = new String[args.length + 2];
        result[0] = regArg1;
        result[1] = regArg2;
        System.arraycopy(args, 0, result, 2, args.length);
        return result;
    }

    public static Object[] test20Args(Object arg1, Object arg2, Object arg3,
            Object arg4, Object arg5, Object arg6, Object arg7, Object arg8,
            Object arg9, Object arg10, Object arg11, Object arg12,
            Object arg13, Object arg14, Object arg15, Object arg16,
            Object arg17, Object arg18, Object arg19, Object arg20) {
        return new Object[] { arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8,
                arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17,
                arg18, arg19, arg20 };
    }

    public static void testRestrictedClassLoader() throws Throwable {
        final Throwable[] t = new Throwable[1];
        Thread thread = new Thread(new Runnable() {

            @Override
            public void run() {
                Jep jep = null;
                try {
                    JepConfig cfg = new JepConfig().setInteractive(true)
                            .setClassLoader(restrictedClassLoader);
                    jep = new Jep(cfg);
                    jep.eval("from java.io import File");
                } catch (Throwable th) {
                    t[0] = th;
                } finally {
                    if (jep != null) {
                        try {
                            jep.close();
                        } catch (JepException e) {
                            throw new RuntimeException(
                                    "Error closing Jep instance", e);
                        }
                    }
                    synchronized (Test.class) {
                        Test.class.notify();
                    }
                }
            }
        });

        synchronized (Test.class) {
            thread.start();
            try {
                Test.class.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        if (t[0] == null) {
            throw new RuntimeException("Did not throw classloader exception!");
        } else if (!t[0].getMessage().contains("ImportError")) {
            throw t[0];
        }
    }

    public static void main(String argv[]) throws Throwable {
        Jep jep = new Jep();
        try {
            jep.runScript("runtests.py");
        } finally {
            jep.close();
        }
    }
} // Test
