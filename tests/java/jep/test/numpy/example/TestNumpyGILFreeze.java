package jep.test.numpy.example;

import jep.Jep;
import jep.JepConfig;
import jep.JepException;

/**
 * A test class that illustrates how numpy's floating point error handling can
 * cause python to deadlock trying to acquire the GIL. More specifically,
 * ufunc_object.c calls NPY_ALLOW_C_API which attempts to acquire the GIL.
 * Python is confused about the thread state and GIL state due to more than one
 * Jep interpreter on the same thread.
 * 
 * Note this problem is only recreatable if you intentionally ignore the JEP
 * THREAD WARNINGS and create two interpreters that coexist on the same thread
 * at the same time.
 * 
 * This test is NOT run by the unittests.
 * 
 * Created: April 2015
 * 
 * @author Nate Jensen
 * @see "https://github.com/numpy/numpy/issues/5856"
 */
public class TestNumpyGILFreeze {

    private static final String UNDERFLOW = "def forceUnderflow():\n"
            + "   a = numpy.array([1, 2], numpy.float32)\n"
            + "   for i in xrange(10):\n" + "      a /= 10000\n"
            + "   print 'python method complete'\n";


    public static void main(String[] args) throws JepException {
        JepConfig cfg = new JepConfig().setInteractive(true);
        Jep jep = null;
        try {
            Jep jep0 = new Jep(cfg);
            jep = new Jep(cfg);
            jep0.close();
            jep.eval("import numpy");
            /*
             * If error conditions are set to ignore, we will not reach the
             * point in ufunc_object.c where NPY_ALLOW_C_API will cause the GIL
             * to hang.
             */
            jep.eval("numpy.seterr(under='warn')");
            jep.eval(UNDERFLOW);
            jep.eval("forceUnderflow()"); // this line will freeze
            System.out.println("returned from python interpreter");
        } catch (JepException e) {
            e.printStackTrace();
        } finally {
            if (jep != null) {
                System.out.println("closing jep interpreter");
                jep.close();
            }
        }
        System.out.println("java main() finished");
    }

}
