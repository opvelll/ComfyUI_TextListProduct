import unittest
from src.PromptPairConcat import PromptPairConcat


class TestPromptPairConcat(unittest.TestCase):
    def setUp(self):
        self.tlc = PromptPairConcat()

    def test_concat_lists(self):
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_a = ["a", "b", "c"]
        list_b = ["1", "2", "3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(
            result,
            (
                [
                    "a,1",
                    "b,2",
                    "c,3",
                ],
            ),
        )

    def test_concat_lists_clean_false(self):
        # クリーン結合をしない場合
        separator = ", "
        isClean = "false"
        trailing_separator = "false"
        list_a = ["a", "b", "c"]
        list_b = ["1", "2", "3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(result, (["a, 1", "b, 2", "c, 3"],))

    def test_concat_lists_uneven_length_clean_true(self):
        # リストの長さが異なる場合、クリーン結合を行う
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_a = ["a", "b"]
        list_b = ["1", "2", "3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(result, (["a,1", "b,2", "3"],))

    def test_concat_lists_uneven_length_clean_false(self):
        # リストの長さが異なる場合、クリーン結合をしない
        separator = ", "
        isClean = "false"
        trailing_separator = "false"
        list_a = ["a", "b"]
        list_b = ["1", "2", "3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(result, (["a, 1", "b, 2", "3"],))

    def test_concat_single_list_a_only(self):
        # list_aのみが指定されている場合
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_a = ["a", "b", "c"]
        result = self.tlc.concat_lists(separator, isClean, trailing_separator, list_a)
        self.assertEqual(result, (["a", "b", "c"],))

    def test_concat_single_list_b_only(self):
        # list_bのみが指定されている場合
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_b = ["1", "2", "3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, None, list_b
        )
        self.assertEqual(result, (["1", "2", "3"],))

    def test_concat_no_lists(self):
        # リストが何も指定されていない場合
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        result = self.tlc.concat_lists(separator, isClean, trailing_separator)
        self.assertEqual(result, ([],))

    def test_concat_with_extra_spaces_and_commas(self):
        # 余分なスペースやカンマを含む場合のクリーン結合
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_a = ["a, ", " b ", "c"]
        list_b = [" 1", "2,", " 3 "]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(
            result,
            (
                [
                    "a,1",
                    "b,2",
                    "c,3",
                ],
            ),
        )

    def test_concat_empty_strings(self):
        # 空文字列がある場合のクリーン結合
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_a = ["", "b", ""]
        list_b = ["1", "", "3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(
            result,
            (
                [
                    "1",
                    "b",
                    "3",
                ],
            ),
        )

    # カンマで区切られた文字列の場合
    def test_concat_lists_with_comma_separated_strings(self):
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_a = ["a, b", "c"]
        list_b = ["1", "2, 3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(
            result,
            (
                [
                    "a,b,1",
                    "c,2,3",
                ],
            ),
        )

    # 最後がカンマと複数のスペースで終わる場合
    def test_concat_lists_with_trailing_comma_and_spaces(self):
        separator = ","
        isClean = "true"
        trailing_separator = "false"
        list_a = ["a, b,    ", "c,    "]
        list_b = ["1", "2, 3"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(
            result,
            (
                [
                    "a,b,1",
                    "c,2,3",
                ],
            ),
        )

    def test_concat_lists_with_trailing_separator_enabled(self):
        separator = " | "
        isClean = "true"
        trailing_separator = "true"
        list_a = ["a", "b"]
        list_b = ["1", "2"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(result, (["a | 1 | ", "b | 2 | "],))

    def test_concat_lists_clean_false_uses_custom_separator(self):
        separator = " | "
        isClean = "false"
        trailing_separator = "false"
        list_a = ["a", "b"]
        list_b = ["1", "2"]
        result = self.tlc.concat_lists(
            separator, isClean, trailing_separator, list_a, list_b
        )
        self.assertEqual(result, (["a | 1", "b | 2"],))
