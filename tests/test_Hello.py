import unittest
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual("Hello", "Hello")


if __name__ == '__main__':
    unittest.main()
