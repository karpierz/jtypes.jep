# coding: utf-8

from __future__ import absolute_import
import unittest
import os
import sys
from jep import findClass
from jep.jdbc import connect
from jep import jdbc as dbapi
from java.lang import Integer, Long, Double, Math
from java.sql import Date, Timestamp, Time

db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data","test.db")  # <AK> improvement


# <AK>: @unittest.skipIf(sys.platform.startswith("win"), "file access issues on Windows")
class TestJdbc(unittest.TestCase):

    jdbc_url = 'jdbc:sqlite:' + db_file.replace("\\","/")  # <AK> fix, was: 'jdbc:sqlite:build/test.db'

    @classmethod
    def setUpClass(cls):
        super(TestJdbc, cls).setUpClass()
        # <AK> fix/improv: moved from module level
        try:
            findClass('org.sqlite.JDBC')
        except:
            raise unittest.SkipTest('JDBC not on classpath')

    def tearDown(self):
        if os.path.exists(db_file):  # <AK> was: 'build/test.db'
            os.remove(db_file)       #           -||-

    def test_java_sql(self):
        """
        regression test

        example and library from: http://www.zentus.com/sqlitejdbc/
        """
        conn = None
        try:
            from java.sql import DriverManager 
            conn = DriverManager.getConnection(self.jdbc_url)

            stat = conn.createStatement()
            stat.executeUpdate("drop table if exists people")
            stat.executeUpdate("create table people (name, occupation)")
            prep = conn.prepareStatement("insert into people values (?, ?)")

            prep.setString(1, "Gandhi")
            prep.setString(2, "politics")
            prep.addBatch()
            prep.setString(1, "Turing")
            prep.setString(2, "computers")
            prep.addBatch()
            prep.setString(1, "Wittgenstein")
            prep.setString(2, "smartypants")
            prep.addBatch()

            conn.setAutoCommit(False)
            prep.executeBatch()
            conn.setAutoCommit(True)

            rs = stat.executeQuery("select * from people")
            self.assertTrue(rs.next())
            self.assertEqual('Gandhi', rs.getString('name'))
            self.assertTrue(rs.next())
            self.assertEqual('Turing', rs.getString('name'))
            self.assertTrue(rs.next())
            self.assertEqual('Wittgenstein', rs.getString('name'))

            self.assertFalse(rs.next())
            self.assertFalse(rs.next())
            self.assertFalse(rs.next())

            rs.close()
            prep.close()
            stat.close()
        finally:
            if conn:
                conn.close()

    def test_dbapi_primitives(self):
        conn = None
        try:
            conn = connect(self.jdbc_url)
            cursor = conn.cursor()

            cursor.execute('''
            create table primitives (
                one integer,
                two_string text,
                three char(10),
                four double,
                five real
                )
            ''')
            
            # Some versions of sqlite are not storing full precision.
            # This is Double.MAX_VALUE, but truncated to 10 digits after the decimal.
            doubleValue = 1.7976931348e+308
            
            cursor.execute('insert into primitives values (?, ?, ?, ?, ?)',
                           Integer.MAX_VALUE,
                           'testé',
                           None,
                           doubleValue,
                           5.6,
                           )
            #*** beg: jtypes extension ***#
            cursor.execute("insert into primitives values (?, ?, ?, ?, ?)",
                           Integer.MAX_VALUE - 1,
                           "bar",
                           None,
                           doubleValue - 1.0,
                           15.8,
                           )
            cursor.execute("insert into primitives values (?, ?, ?, ?, ?)",
                           Integer.MAX_VALUE - 3,
                           "foo",
                           None,
                           doubleValue - 3.0,
                           34.9,
                           )
            #*** end: jtypes extension ***#
            cursor.execute('select * from primitives')
            row = cursor.fetchone()

            self.assertEqual(row[0], Integer.MAX_VALUE)
            self.assertEqual(cursor.description[0][0], 'one')
            self.assertEqual(cursor.description[0][1], 4)  # sql type integer

            self.assertEqual(row[1], 'testé')
            self.assertEqual(cursor.description[1][0], 'two_string')

            self.assertIsNone(row[2])
            self.assertEqual(cursor.description[2][0], 'three')

            self.assertEqual(row[3], doubleValue)
            self.assertEqual(cursor.description[3][0], 'four')

            self.assertEqual(row[4], 5.6)
            self.assertEqual(cursor.description[4][0], 'five')

            #*** beg: jtypes extension ***#

            row = cursor.fetchmany(1)[0]

            self.assertEqual(row[0], Integer.MAX_VALUE - 1)
            self.assertEqual(cursor.description[0][0], "one")
            self.assertEqual(cursor.description[0][1], 4)  # sql type integer

            self.assertEqual(row[1], "bar")
            self.assertEqual(cursor.description[1][0], "two_string")

            self.assertIsNone(row[2])
            self.assertEqual(cursor.description[2][0], "three")

            self.assertEqual(row[3], doubleValue - 1.0)
            self.assertEqual(cursor.description[3][0], "four")

            self.assertEqual(row[4], 15.8)
            self.assertEqual(cursor.description[4][0], "five")

            row = cursor.fetchall()[0]

            self.assertEqual(row[0], Integer.MAX_VALUE - 3)
            self.assertEqual(cursor.description[0][0], "one")
            self.assertEqual(cursor.description[0][1], 4) # sql type integer

            self.assertEqual(row[1], "foo")
            self.assertEqual(cursor.description[1][0], "two_string")

            self.assertIsNone(row[2])
            self.assertEqual(cursor.description[2][0], "three")

            self.assertEqual(row[3], doubleValue - 3.0)
            self.assertEqual(cursor.description[3][0], "four")

            self.assertEqual(row[4], 34.9)
            self.assertEqual(cursor.description[4][0], "five")

            #*** end: jtypes extension ***#

            cursor.close()
        finally:
            if conn:
                conn.close()

    def test_datetime(self):
        conn = None
        try:
            conn = connect(self.jdbc_url)
            cursor = conn.cursor()

            cursor.execute('''
            create table dt (
                one date,
                two date,
                three time,
                four time,
                five timestamp
                )
            ''')

            cursor.execute('insert into dt values (?, ?, ?, ?, ?)',
                           dbapi.Date(2012, 6, 1),
                           Date(1338534000000),
                           Time(1),
                           dbapi.Time(1, 2, 3),
                           dbapi.Timestamp(2012, 6, 1, 1, 2, 3),
                           )
            cursor.execute('select * from dt')

            # crazy sqllite doesn't have normal date types.
            # this will force jep.jdbc to interpret the result correctly for this
            # test.
            cursor.description = (
                ('one', 91, None, None, None, None, True),
                ('two', 91, None, None, None, None, True),
                ('three', 92, None, None, None, None, True),
                ('four', 92, None, None, None, None, True),
                ('five', 93, None, None, None, None, True),
            )
            row = cursor.fetchone()

            self.assertEqual(row[0].toString(), '2012-06-01')
            self.assertEqual(row[1].getTime(), 1338534000000)
            self.assertEqual(row[2].getTime(), 1)
            self.assertEqual(row[3].toString(), '01:02:03')
            self.assertEqual(row[4].toString(), '2012-06-01 01:02:03.0')
            cursor.close()
        finally:
            if conn:
                conn.close()

    def test_batch(self):
        conn = None
        try:
            conn = connect(self.jdbc_url)
            cursor = conn.cursor()

            cursor.execute('create table batch ( one integer )')

            cursor.executemany('insert into batch values (?)', [
                (1,),
                (2,),
                (3,),
            ])

            cursor.execute('select sum(one) from batch')
            row = cursor.fetchone()
            self.assertEqual(row[0], 6)
            cursor.close()
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    unittest.main()
