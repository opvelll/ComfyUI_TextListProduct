import unittest

from src.ProductedString import ProductedString


class TestProductedString(unittest.TestCase):
    def setUp(self):
        self.node = ProductedString()

    def test_combine_input_lists_two_lists(self):
        result = self.node.combine_input_lists(
            ", ", "\n", list_a=["a", "b"], list_b=["1", "2"]
        )
        self.assertEqual(result, ("a, 1\na, 2\nb, 1\nb, 2",))

    def test_combine_input_lists_only_connected_lists_are_used(self):
        result = self.node.combine_input_lists(
            " | ",
            "\n",
            list_a=["a"],
            list_c=["1", "2"],
            list_f=["x"],
            ignored="not-a-list",
        )
        self.assertEqual(result, ("a | 1 | x\na | 2 | x",))

    def test_combine_input_lists_empty_when_no_lists_are_connected(self):
        result = self.node.combine_input_lists(", ", "\n")
        self.assertEqual(result, ("",))

    def test_combine_input_lists_filters_empty_strings(self):
        result = self.node.combine_input_lists(
            ", ", "\n", list_a=["a", ""], list_b=["1", ""]
        )
        self.assertEqual(result, ("a, 1\na\n1",))

    def test_combine_input_lists_uses_custom_newline_character(self):
        result = self.node.combine_input_lists(
            ", ", " / ", list_a=["a"], list_b=["1", "2"]
        )
        self.assertEqual(result, ("a, 1 / a, 2",))


if __name__ == "__main__":
    unittest.main()
