import unittest

from Day1.Day1 import Day1
from Day1.Day1Part2 import Day2


class TestDay1(unittest.TestCase):
    def setUp(self):
        self.day = Day1()

    def test_findDistance(self):
        test_list1 = [1,2,3,3,3,4]
        test_list2 = [3,3,3,4,5,9]

        result = self.day.findDistance(test_list1, test_list2)
        print(result)
        self.assertEqual(result, 11)

class TestDay2(unittest.TestCase):
    def setUp(self):
        self.day = Day2()

    def test_findSimilarity(self):
        test_list1 = [3,4,2,1,3,3]
        test_list2 = [4,3,5,3,9,3]
        result = self.day.findSimScore(test_list1, test_list2)
        self.assertEqual(result, 31)



if __name__ == '__main__':
    unittest.main()
