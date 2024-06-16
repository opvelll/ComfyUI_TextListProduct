import unittest
from TextListProduct import TextListProduct


class TestTextListProduct(unittest.TestCase):
    def setUp(self):
        self.tlp = TextListProduct()

    def test_combine_input_lists(self):
        list_a = ['a', 'b', 'c']
        list_b = ['1', '2', '3']
        separator = ', '
        expected_result = ['a, 1', 'a, 2', 'a, 3', 'b, 1',
                           'b, 2', 'b, 3', 'c, 1', 'c, 2', 'c, 3']
        result = self.tlp.combine_input_lists(list_a, list_b, separator)
        self.assertEqual(result, (expected_result,))

    # list_aが一つの場合
    def test_combine_input_lists_one_list(self):
        list_a = ['a']
        list_b = ['1', '2', '3']
        separator = ', '
        expected_result = ['a, 1', 'a, 2', 'a, 3']
        result = self.tlp.combine_input_lists(list_a, list_b, separator)
        self.assertEqual(result, (expected_result,))


if __name__ == '__main__':
    unittest.main()
