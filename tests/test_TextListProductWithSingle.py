import unittest
from src.TextListProductWithSingleA import TextListProductWithSingleA
from src.TextListProductWithSingleB import TextListProductWithSingleB
from src.TextListProductWithSingleBoth import TextListProductWithSingleBoth


class TestTextListProductWithSingle(unittest.TestCase):
    def setUp(self):
        self.tlp_single_a = TextListProductWithSingleA()
        self.tlp_single_b = TextListProductWithSingleB()
        self.tlp_single_both = TextListProductWithSingleBoth()

    # TextListProductWithSingleA一般的なケース
    def test_combine_input_lists_with_single_a(self):
        list_a = ["a", "b", "c"]
        list_b = ["1", "2", "3"]
        separator = ", "
        expected_result = [
            "a",
            "a, 1",
            "a, 2",
            "a, 3",
            "b",
            "b, 1",
            "b, 2",
            "b, 3",
            "c",
            "c, 1",
            "c, 2",
            "c, 3",
        ]
        result = self.tlp_single_a.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # TextListProductWithSingleB一般的なケース
    def test_combine_input_lists_with_single_b(self):
        list_a = ["a", "b", "c"]
        list_b = ["1", "2", "3"]
        separator = ", "
        expected_result = [
            "1",
            "2",
            "3",
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
        result = self.tlp_single_b.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))

    # TextListProductWithSingleBoth一般的なケース
    def test_combine_input_lists_with_single_both(self):
        list_a = ["a", "b", "c"]
        list_b = ["1", "2", "3"]
        separator = ", "
        expected_result = [
            "1",
            "2",
            "3",
            "a",
            "a, 1",
            "a, 2",
            "a, 3",
            "b",
            "b, 1",
            "b, 2",
            "b, 3",
            "c",
            "c, 1",
            "c, 2",
            "c, 3",
        ]
        result = self.tlp_single_both.combine_input_lists(separator, list_a, list_b)
        self.assertEqual(result, (expected_result,))


if __name__ == "__main__":
    unittest.main()
