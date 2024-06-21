import unittest
from src.TextListProduct import TextListProduct


class TestTextListProduct(unittest.TestCase):
    def setUp(self):
        self.tlp = TextListProduct()

    # 一般的なケース
    def test_combine_input_lists(self):
        list_a = ["a", "b", "c"]
        list_b = ["1", "2", "3"]
        separator = ", "
        expected_result = [
            "a, 1",
            "a, 2",
            "a, 3",
            "b, 1",
            "b, 2",
            "b, 3",
            "c, 1",
            "c, 2",
            "c, 3",
        ]
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # list_aが一つの場合
    def test_combine_input_lists_one_list(self):
        list_a = ["a"]
        list_b = ["1", "2", "3"]
        separator = ", "
        expected_result = ["a, 1", "a, 2", "a, 3"]
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # list_bが一つの場合
    def test_combine_input_lists_one_list_b(self):
        list_a = ["a", "b", "c"]
        list_b = ["1"]
        separator = ", "
        expected_result = ["a, 1", "b, 1", "c, 1"]
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # list_aが空の場合
    def test_combine_input_lists_empty_list_a(self):
        list_a = []
        list_b = ["1", "2", "3"]
        separator = ", "
        expected_result = []
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # list_aとlist_bが空の場合
    def test_combine_input_lists_empty(self):
        list_a = []
        list_b = []
        separator = ", "
        expected_result = []
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # list_aに空文字列が含まれる場合
    def test_combine_input_lists_empty_element(self):
        list_a = ["a", "", "c"]
        list_b = ["1", "2", "3"]
        separator = ", "
        expected_result = [
            "a, 1",
            "a, 2",
            "a, 3",
            "1",
            "2",
            "3",
            "c, 1",
            "c, 2",
            "c, 3",
        ]
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # list_bに空文字列が含まれる場合
    def test_combine_input_lists_empty_element_b(self):
        list_a = ["a", "b", "c"]
        list_b = ["1", "", "3"]
        separator = ", "
        expected_result = [
            "a, 1",
            "a",
            "a, 3",
            "b, 1",
            "b",
            "b, 3",
            "c, 1",
            "c",
            "c, 3",
        ]
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # list_aとlist_bに空文字列が含まれる場合
    def test_combine_input_lists_empty_element_both(self):
        list_a = ["a", "", "c"]
        list_b = ["1", "", "3"]
        separator = ", "
        expected_result = ["a, 1", "a", "a, 3", "1", "3", "c, 1", "c", "c, 3"]
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # separatorが空文字列の場合
    def test_combine_input_lists_empty_separator(self):
        list_a = ["a", "b", "c"]
        list_b = ["1", "2", "3"]
        separator = ""
        expected_result = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        result = self.tlp.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))


if __name__ == "__main__":
    unittest.main()
