import unittest

from Day1 import Day1


class TestDay1(unittest.TestCase):
    def setUp(self):
        self.day = Day1()

    def test_findDistance(self):
        test_list1 = [1,2,3,3,3,4]
        test_list2 = [3,3,3,4,5,9]

        result = self.day.findDistance(test_list1, test_list2)
        print(result)
        self.assertEqual(result, 11)




if __name__ == '__main__':
    unittest.main()
