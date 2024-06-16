import itertools


class TextListProductWithSingleBoth:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "list_a": ("LIST", {"forceInput": True}),
                "list_b": ("LIST", {"forceInput": True}),
                "separator": ("STRING", {"default": ", "}),
            },
        }

    def combine_input_lists(self, list_a, list_b, separator):
        return (self.join_filtered_lists(list_a, list_b, separator),)

    def join_filtered_lists(self, list_a, list_b, separator) -> list[str]:
        return list(map(separator.join, self.get_filtered_product(list_a, list_b)))

    def get_filtered_product(self, list_a, list_b):
        return [filter(None, x) for x in itertools.product([''] + list_a, [''] + list_b)]

    RETURN_NAMES = ("list",)
    RETURN_TYPES = ("LIST",)
    FUNCTION = "combine_input_lists"
    CATEGORY = "textProduct"
