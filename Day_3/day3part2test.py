import unittest

from day3part2 import *

class test(unittest.TestCase):
    file1 = open("testinput.txt","r")
    file2 = open("puzzleinput.txt","r")

    def test_tonto(self):
        self.assertEqual(2,1+1)

    def test_1(self):
        self.assertEqual(Rucksack.calculate(test.file1),70)

    def test_real(self):
        self.assertEqual(Rucksack.calculate(test.file2),1)


if __name__ == "__main__":
    unittest.main()