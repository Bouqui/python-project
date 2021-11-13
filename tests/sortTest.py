import unittest
from pages import sortPage

class sortTest(unittest.TestCase):


    def test_sort(self):
        string = sortPage.sortPage.sortString("kOJkdsmdb%$8jj10")
        self.assertEqual(string, "810smkkjjddbOJ%$")
        print(string)

    def test_sort1(self):
        string = sortPage.sortPage.sortString("A11a4")
        self.assertEqual(string, "411aA")
        print(string)