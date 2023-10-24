import unittest
from main import Comp


class MyTestCase(unittest.TestCase):
    
     def test_add(self):
        value = Comp(2,3).add()
        self.assertEqual(value, 5)


if __name__ == '__main__':
    unittest.main()
