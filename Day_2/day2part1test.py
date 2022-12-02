import unittest

from day2part1 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(PPT.calculo(test.file1),15)

    def test_real(self):
        self.assertEqual(PPT.calculo(test.file2),15523)


if __name__ == "__main__":
    unittest.main()