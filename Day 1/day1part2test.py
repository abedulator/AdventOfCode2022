import unittest

from day1part2 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(Calorias.calculo(test.file1),45000)

    def test_real(self):
        self.assertEqual(Calorias.calculo(test.file2),213958)


if __name__ == "__main__":
    unittest.main()