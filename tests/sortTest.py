import unittest
from pages import sortPage

class sortTest(unittest.TestCase):


    def test_sort(self):
        string = sortPage.sortPage.sortString("kOJkdsmdb%$8jj10")
        self.assertEqual(string, "810smkkjjddbOJ%$")
        print(string)