import unittest

from src.StringsToList import StringsToList


class TestStringsToList(unittest.TestCase):
    def setUp(self):
        self.node = StringsToList()

    def test_collects_strings_in_input_order(self):
        result = self.node.collect_strings(
            text_g="seven", text_a="one", text_d="four"
        )
        self.assertEqual(result, (["one", "four", "seven"],))

    def test_preserves_connected_empty_strings(self):
        result = self.node.collect_strings(text_a="alpha", text_b="", text_c="gamma")
        self.assertEqual(result, (["alpha", "", "gamma"],))

    def test_no_connected_inputs_returns_empty_list(self):
        result = self.node.collect_strings()
        self.assertEqual(result, ([],))

    def test_node_definition(self):
        input_types = self.node.INPUT_TYPES()
        self.assertEqual(input_types["required"], {})
        self.assertEqual(
            list(input_types["optional"].keys()),
            [f"text_{suffix}" for suffix in "abcdefg"],
        )
        for input_type in input_types["optional"].values():
            self.assertEqual(input_type, ("STRING", {"forceInput": True}))
        self.assertEqual(self.node.RETURN_TYPES, ("LIST",))
        self.assertEqual(self.node.CATEGORY, "TextListProduct")
        self.assertFalse(hasattr(self.node, "OUTPUT_IS_LIST"))


if __name__ == "__main__":
    unittest.main()
