from itertools import chain, zip_longest


class PromptPairConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "separator": ("STRING", {"default": ","}),
                "isClean": (["true", "false"],),
            },
            "optional": {
                "list_a": ("LIST", {"forceInput": True}),
                "list_b": ("LIST", {"forceInput": True}),
            },
        }

    def concat_lists(self, separator, isClean, list_a=None, list_b=None):
        lists = [lst for lst in [list_a, list_b] if isinstance(lst, list)]
        if len(lists) == 1:
            return (lists[0],)

        if isClean == "true":
            return (
                [
                    self.clean_and_concat(separator, a, b)
                    for a, b in zip_longest(*lists, fillvalue="")
                ],
            )

        return ([a + b for a, b in zip_longest(*lists, fillvalue="")],)

    def clean_and_concat(self, separator, *args):
        # 各要素から不要な空白とカンマを取り除く
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
        # ", "で連結し、最後に", "を追加
        return ", ".join(cleaned_args + [""])

    RETURN_NAMES = ("list",)
    RETURN_TYPES = ("LIST",)
    FUNCTION = "concat_lists"
    CATEGORY = "TextListProduct"
