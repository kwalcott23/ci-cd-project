import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
