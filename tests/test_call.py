from __future__ import absolute_import
import unittest

import jt.jep as jep
Test = jep.findClass('jep.test.Test')
Boolean = jep.findClass('java.lang.Boolean')
StringBuilder = jep.findClass('java.lang.StringBuilder')
ArrayList = jep.findClass('java.util.ArrayList')


class TestTypes(unittest.TestCase):

    def setUp(self):
        self.test = Test()

    def test_enum(self):
        testEnum = self.test.getEnum()
        self.assertEqual(0, testEnum.ordinal())

    def test_getstring_array(self):
        obj = self.test.getStringArray()
        self.assertEqual('one', obj[0])
        self.assertEqual('two', obj[1])
        self.assertEqual('one two', ' '.join(obj))

    def test_string_string_array(self):
        obj = self.test.getStringStringArray()
        self.assertEqual('one', obj[0][0])

    def test_int_array(self):
        obj = self.test.getIntArray()
        self.assertEqual(1, obj[0])

    def test_bool_array(self):
        obj = self.test.getBooleanArray()
        self.assertTrue(obj[1])

    def test_short_array(self):
        obj = self.test.getShortArray()
        self.assertEqual(123, obj[0])

    def test_float_array(self):
        obj = self.test.getFloatArray()
        self.assertAlmostEqual(123.12300109863281, obj[0])

    def test_booleanobj(self):
        self.assertTrue(self.test.getClassBoolean().booleanValue())

    def test_characterobj(self):
        self.assertEqual('x', self.test.getClassCharacter().charValue())

    def test_byteobj(self):
        self.assertEqual(45, self.test.getClassByte().byteValue())

    def test_shortobj(self):
        self.assertEqual(31580, self.test.getClassShort().shortValue())

    def test_intobj(self):
        self.assertEqual(-2147483648, self.test.getClassInteger().intValue())

    def test_long(self):
        self.assertEqual(9223372036854775807, self.test.getClassLong().longValue())

    def test_float(self):
        self.assertAlmostEqual(3.4028234663852886e+38, self.test.getClassFloat().floatValue())

    def test_double(self):
        self.assertEqual(4.9E-324, self.test.getClassDouble().doubleValue())

    def test_string(self):
        self.assertEqual("toString(). Thanks for calling Java(tm).", self.test.toString())

    def test_getobj(self):
        obj = self.test.getObject()
        self.assertEqual("list 0", str(obj.get(0)))

    def test_character_array(self):
        obj = self.test.getCharArray()
        self.assertEqual('r', obj[0])

    def test_byte_array(self):
        obj = self.test.getByteArray()
        self.assertEqual(45, obj[0])

    def test_long_array(self):
        obj = self.test.getLongArray()
        self.assertEqual(6289234456854775807, obj[0])

    def test_double_array(self):
        obj = self.test.getDoubleArray()
        self.assertAlmostEqual(6.873E-248, obj[0])

    def test_string_array(self):
        obj = self.test.getStringArray()
        self.assertEqual("one", obj[0])
        self.assertEqual("two", obj[1])
        self.assertEqual("one two", " ".join(obj))

    def test_object_array(self):
        obj = self.test.getObjectArray()
        self.assertEqual(self.test.toString(), obj[0].toString())

    def test_equals(self):
        self.assertTrue(self.test.getClass() == Test)
        from java.lang import Class, String, Integer
        self.assertFalse(self.test.getClass() == Class)
        self.assertEqual(String('one'), String('one'))
        self.assertTrue(String('1') == String('1'))
        self.assertEqual(self.test, self.test)
        self.assertNotEqual(self.test, Test())
        self.assertNotEqual(String('two'), String('one'))

        self.assertEqual(String, String)
        self.assertNotEqual(String, Integer)

    def test_boxing(self):
        self.assertTrue(Boolean.TRUE.equals(True))
        self.assertFalse(Boolean.TRUE.equals(1))
        self.assertFalse(Boolean.TRUE.equals(1.5))

    def test_20args(self):
        args = list()
        for x in range(20):
            args.append(Test())
        result = Test.test20Args(*args)
        self.assertEqual(args, list(result))

    def test_deepList(self):
        # Make sure type conversion works when a list contains a list...
        l = [self.test]
        for i in range(50):
            l = [l]
        result = self.test.testObjectPassThrough(l)
        for i in range(50):
            result = result[0]
        self.assertEquals(self.test, result[0])

    def test_overload(self):
        builder = StringBuilder()
        builder.append(1)
        self.assertTrue(builder.toString() == "1")
        builder = StringBuilder()
        builder.append(StringBuilder)
        self.assertTrue(builder.toString() == "class java.lang.StringBuilder")
        list = ArrayList()
        list.add("One")
        list.add("Two")
        list.add("Three")
        list.remove(1)
        self.assertEqual(list.size(), 2)
