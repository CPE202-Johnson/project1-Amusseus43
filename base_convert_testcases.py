import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(0,2),"0")
        self.assertEqual(convert(1000,2),"1111101000")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        self.assertEqual(convert(0,4),"0")
        self.assertEqual(convert(1000,4),"33220")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(0,16),"0")
        self.assertEqual(convert(1000,16),"3E8")

if __name__ == "__main__":
        unittest.main()