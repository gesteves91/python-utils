
import unittest
from utils import countElementsList
 
class TestUtils(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_count_elements(self):
        list = ["a", "b", "c", "d"]

        self.assertEqual(countElementsList(list), 4)
 
if __name__ == '__main__':
    unittest.main()