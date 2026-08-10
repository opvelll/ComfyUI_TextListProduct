import unittest

from src.MultilineStringToList import MultilineStringToList


class TestMultilineStringToList(unittest.TestCase):
    def setUp(self):
        self.node = MultilineStringToList()

    def test_converts_multiline_text_with_default_cleanup(self):
        result = self.node.convert_to_list("  alpha  \n\n beta\n   \ngamma  ")
        self.assertEqual(result, (["alpha", "beta", "gamma"],))

    def test_supports_crlf_and_cr_line_endings(self):
        result = self.node.convert_to_list("alpha\r\nbeta\rgamma")
        self.assertEqual(result, (["alpha", "beta", "gamma"],))

    def test_trailing_line_ending_does_not_add_empty_item(self):
        result = self.node.convert_to_list("alpha\nbeta\n", keep_empty_lines=True)
        self.assertEqual(result, (["alpha", "beta"],))

    def test_empty_text_returns_empty_list(self):
        result = self.node.convert_to_list("")
        self.assertEqual(result, ([],))

    def test_comment_like_lines_are_preserved(self):
        result = self.node.convert_to_list("# comment\n// comment\nvalue")
        self.assertEqual(result, (["# comment", "// comment", "value"],))

    def test_can_preserve_whitespace(self):
        result = self.node.convert_to_list(
            "  alpha  \n beta ", trim_whitespace=False
        )
        self.assertEqual(result, (["  alpha  ", " beta "],))

    def test_can_preserve_empty_lines_after_trimming(self):
        result = self.node.convert_to_list(
            " alpha \n   \nbeta", keep_empty_lines=True
        )
        self.assertEqual(result, (["alpha", "", "beta"],))

    def test_can_preserve_whitespace_and_empty_lines(self):
        result = self.node.convert_to_list(
            " alpha \n\n   \nbeta",
            trim_whitespace=False,
            keep_empty_lines=True,
        )
        self.assertEqual(result, ([" alpha ", "", "   ", "beta"],))

    def test_node_definition(self):
        input_types = self.node.INPUT_TYPES()
        self.assertEqual(input_types["required"]["text"][0], "STRING")
        self.assertTrue(input_types["required"]["text"][1]["multiline"])
        self.assertTrue(
            input_types["required"]["trim_whitespace"][1]["default"]
        )
        self.assertFalse(
            input_types["required"]["keep_empty_lines"][1]["default"]
        )
        self.assertEqual(self.node.RETURN_TYPES, ("LIST",))
        self.assertEqual(self.node.CATEGORY, "TextListProduct")
        self.assertFalse(hasattr(self.node, "OUTPUT_IS_LIST"))


if __name__ == "__main__":
    unittest.main()
