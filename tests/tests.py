import unittest
from main import Comp


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        value = Comp.add(2,3)
        self.assertEqual(value, 18)


if __name__ == '__main__':
    unittest.main()
