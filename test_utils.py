
import unittest
from utils import countElementsList
from utils import calcultateSatisfaction
 
class TestUtils(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_count_elements(self):
        list = ["a", "b", "c", "d"]

        self.assertEqual(countElementsList(list), 4)

    def test_satisfactions(self):
        low_review = 80
        high_review = 100
        medium_review = 95

        self.assertEqual(calcultateSatisfaction(low_review), 0)
        self.assertEqual(calcultateSatisfaction(high_review), 1)
        self.assertEqual(calcultateSatisfaction(medium_review), 1)

if __name__ == '__main__':
    unittest.main()