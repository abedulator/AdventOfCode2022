import unittest

from day11part1 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(Monkey.calculate(test.file1),10605)

    def test_real(self):
        self.assertEqual(Monkey.calculate(test.file2),1)


if __name__ == "__main__":
    unittest.main()