import unittest

from day7part2 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(Directories.calculate(test.file1),24933642)

    def test_real(self):
        self.assertEqual(Directories.calculate(test.file2),1815525)


if __name__ == "__main__":
    unittest.main()