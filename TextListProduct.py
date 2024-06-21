import itertools

from BaseTextListProduct import BaseTextListProduct


class TextListProduct(BaseTextListProduct):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "separator": ("STRING", {"default": ", "}),
                "list_a": ("LIST", {"forceInput": True}),
                "list_b": ("LIST", {"forceInput": True}),
            },
        }

    def combine_input_lists(self, separator, list_a, list_b):
        return (list(self.join_filtered_lists(separator, list_a, list_b)),)

    RETURN_NAMES = ("list",)
    RETURN_TYPES = ("LIST",)
    FUNCTION = "combine_input_lists"
    CATEGORY = "TextListProduct"
