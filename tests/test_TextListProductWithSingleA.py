
import unittest
from TextListProductWithSingleA import TextListProductWithSingleA


class TestTextListProductWithSingleA(unittest.TestCase):
    def setUp(self):
        self.combiner = TextListProductWithSingleA()

    def test_join_filtered_lists(self):
        list_a = ['a', 'b']
        list_b = ['1', '2']
        separator = ', '
        expected_result = ['a', 'a, 1', 'a, 2', 'b', 'b, 1', 'b, 2']
        result = self.combiner.join_filtered_lists(list_a, list_b, separator)
        self.assertEqual(result, expected_result)

    # list_a = []
    def test_join_filtered_lists_empty_list_a(self):
        list_a = []
        list_b = ['1', '2']
        separator = ', '
        expected_result = []
        result = self.combiner.join_filtered_lists(list_a, list_b, separator)
        self.assertEqual(result, expected_result)

    # list_a = ['']
    def test_join_filtered_lists_emptyString_list_a(self):
        list_a = ['']
        list_b = ['1', '2']
        separator = ', '
        expected_result = ['', '1', '2']
        result = self.combiner.join_filtered_lists(list_a, list_b, separator)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
