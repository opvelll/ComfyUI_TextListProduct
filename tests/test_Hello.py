import unittest


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual("Hello", "Hello")


if __name__ == "__main__":
    unittest.main()
