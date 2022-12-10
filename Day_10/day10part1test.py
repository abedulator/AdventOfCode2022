import unittest

from day10part1 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)
    
    def test_1(self):
        self.assertEqual(Tube.calculate(test.file1),13140)

    def test_real(self):
        self.assertEqual(Tube.calculate(test.file2),17180)


if __name__ == "__main__":
    unittest.main()