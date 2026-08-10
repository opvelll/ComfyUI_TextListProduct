import unittest

from src.TextListToSequence import TextListToSequence


class TestTextListToSequence(unittest.TestCase):
    def setUp(self):
        self.node = TextListToSequence()

    def test_preserves_order_and_empty_strings(self):
        text_list = ["alpha", "", "gamma"]
        result = self.node.convert_to_sequence(text_list)
        self.assertEqual(result, (text_list,))
        self.assertIs(result[0], text_list)

    def test_empty_list_raises_clear_error(self):
        with self.assertRaisesRegex(
            ValueError, "requires at least one item.*empty sequential list"
        ):
            self.node.convert_to_sequence([])

    def test_non_string_item_reports_its_index(self):
        with self.assertRaisesRegex(TypeError, "string at index 1, got int"):
            self.node.convert_to_sequence(["alpha", 42, "gamma"])

    def test_non_list_input_reports_its_type(self):
        with self.assertRaisesRegex(TypeError, "expected a list, got tuple"):
            self.node.convert_to_sequence(("alpha", "beta"))

    def test_node_definition(self):
        input_types = self.node.INPUT_TYPES()
        self.assertEqual(
            input_types["required"]["text_list"],
            ("LIST", {"forceInput": True}),
        )
        self.assertEqual(self.node.RETURN_NAMES, ("string",))
        self.assertEqual(self.node.RETURN_TYPES, ("STRING",))
        self.assertEqual(self.node.OUTPUT_IS_LIST, (True,))
        self.assertEqual(self.node.FUNCTION, "convert_to_sequence")
        self.assertEqual(self.node.CATEGORY, "TextListProduct")
        self.assertFalse(hasattr(self.node, "INPUT_IS_LIST"))


if __name__ == "__main__":
    unittest.main()
