import unittest

from day1part1 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(Calorias.calculo(test.file1),24000)

    def test_real(self):
        self.assertEqual(Calorias.calculo(test.file2),73211)


if __name__ == "__main__":
    unittest.main()