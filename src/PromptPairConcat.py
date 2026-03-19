from itertools import chain, zip_longest


class PromptPairConcat:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "separator": ("STRING", {"default": ","}),
                "isClean": (["true", "false"],),
                "trailing_separator": (["false", "true"],),
            },
            "optional": {
                "list_a": ("LIST", {"forceInput": True}),
                "list_b": ("LIST", {"forceInput": True}),
            },
        }

    def concat_lists(
        self, separator, isClean, trailing_separator="false", list_a=None, list_b=None
    ):
        lists = [lst for lst in [list_a, list_b] if isinstance(lst, list)]
        if len(lists) == 1:
            return (lists[0],)
        if len(lists) == 0:
            return ([],)

        append_trailing_separator = trailing_separator == "true"

        if isClean == "true":
            return (
                [
                    self.clean_and_concat(
                        separator, append_trailing_separator, a, b
                    )
                    for a, b in zip_longest(*lists, fillvalue="")
                ],
            )

        return (
            [
                self.concat_pair(separator, append_trailing_separator, a, b)
                for a, b in zip_longest(*lists, fillvalue="")
            ],
        )

    def concat_pair(self, separator, trailing_separator, *args):
        parts = [arg for arg in args if arg != ""]
        result = separator.join(parts)
        if result and trailing_separator:
            return result + separator
        return result

    def clean_and_concat(self, separator, trailing_separator, *args):
        # 各要素から不要な空白とセパレータを取り除く
        cleaned_args = list(
            filter(
                lambda x: x != "",
                map(
                    lambda x: x.strip(),
                    chain.from_iterable(
                        arg.rstrip(separator).split(separator) for arg in args
                    ),
                ),
            )
        )
        result = separator.join(cleaned_args)
        if result and trailing_separator:
            return result + separator
        return result

    RETURN_NAMES = ("list",)
    RETURN_TYPES = ("LIST",)
    FUNCTION = "concat_lists"
    CATEGORY = "TextListProduct"
