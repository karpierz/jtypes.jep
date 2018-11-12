package jep.test.numpy.example;

import jep.Jep;
import jep.JepConfig;
import jep.JepException;

/**
 * A test class that illustrates scipy locking up the thread when there are two
 * sub-interpreters on the same thread.
 * 
 * Note this problem is only recreatable if you intentionally ignore the JEP
 * THREAD WARNINGS and create two interpreters that coexist on the same thread
 * at the same time.
 * 
 * This test is NOT run by the unittests.
 * 
 * Created: July 2015
 * 
 * @author Nate Jensen
 */
public class TestScipyFreeze {

    public static void main(String[] args) {
        try (Jep jep0 = new Jep(new JepConfig().setInteractive(true));
                Jep jep = new Jep(new JepConfig().setInteractive(true))) {
            jep0.eval("from scipy.special import erf");

            // this line will freeze
            jep.eval("from scipy.special import erf");
            System.out.println("returned from python interpreters");
        } catch (JepException e) {
            e.printStackTrace();
        }
        System.out.println("java main() finished");
    }

}
