import unittest

from day5part1 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(Crane.calculate(test.file1),"CMZ")

    def test_real(self):
        self.assertEqual(Crane.calculate(test.file2),"VRWBSFZWM")


if __name__ == "__main__":
    unittest.main()