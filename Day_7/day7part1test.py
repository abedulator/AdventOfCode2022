import unittest

from day7part1 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(Directories.calculate(test.file1),95437)

    def test_real(self):
        self.assertEqual(Directories.calculate(test.file2),1648397)


if __name__ == "__main__":
    unittest.main()