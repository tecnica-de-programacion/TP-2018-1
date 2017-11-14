import unittest
from main import Formater
# import sys
# sys.tracebacklimit = 0

class TestFormater(unittest.TestCase):

    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_clean_integers(self):
        """-- Test Clean Integers"""
        msg = "The correct numerical value is not being returned"
        self.assertEqual(Formater.clean_number('9,000 000'), 9000000, msg=msg)
        self.assertEqual(Formater.clean_number('5'), 5, msg=msg)
        self.assertEqual(Formater.clean_number('58, 710, 520'), 58710520, msg=msg)

    def test_correct_int_cast(self):
        """-- Test Int Cast"""
        msg = "The correct type is not being returned for the integers"
        self.assertTrue(type(Formater.clean_number('9,000 000')) is int, msg=msg)
        self.assertTrue(type(Formater.clean_number('5')) is int, msg=msg)
        self.assertTrue(type(Formater.clean_number('58, 710, 520')) is int, msg=msg)

    def test_clean_floats(self):
        """-- Test Clean Floats"""
        msg = "The numerical value for floating is not being returned"
        self.assertEqual(Formater.clean_number('16,070.45'), float(16070.45), msg=msg)
        self.assertEqual(Formater.clean_number('58, 710.520'), float(58710.520), msg=msg)
        self.assertEqual(Formater.clean_number('16.5'), float(16.5), msg=msg)

    def test_correct_float_cast(self):
        """-- Test Floats Cast"""
        msg = "The correct value for Floats is not returned"
        self.assertTrue(type(Formater.clean_number('16,070.45')) is float, msg=msg)
        self.assertTrue(type(Formater.clean_number('58, 710.520')) is float, msg=msg)
        self.assertTrue(type(Formater.clean_number('16.5')) is float, msg=msg)

    def test_comma_afther_dot(self):
        """-- Test Commas afther dot"""
        msg = "When there are commas after the decimal point, return None.    Example: 13.15,31"
        self.assertEqual(Formater.clean_number('7,000.00,00'), None, msg=msg)
        self.assertEqual(Formater.clean_number('13.15,31'), None, msg=msg)

    def test_no_valid_entrys(self):
        """-- Test No Valid Entrys"""
        msg = "None must be returned for entries that do not comply with the pattern"
        self.assertEqual(Formater.clean_number('#166'), None, msg=msg)
        self.assertEqual(Formater.clean_number('hola'), None, msg=msg)
        self.assertEqual(Formater.clean_number('------'), None, msg=msg)

    def test_multiple_dots(self):
        """-- Test Multiples dots"""
        msg = "None should be returned if there are more than 2 decimal points"
        self.assertEqual(Formater.clean_number('166.66.66'), None, msg=msg)
