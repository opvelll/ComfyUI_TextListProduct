import itertools


class ProductedString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "separator": ("STRING", {"default": ", "}),
                "newline_char": ("STRING", {"default": "\n"}),
            },
            "optional": {
                "list_a": ("LIST", {"forceInput": True}),
                "list_b": ("LIST", {"forceInput": True}),
                "list_c": ("LIST", {"forceInput": True}),
                "list_d": ("LIST", {"forceInput": True}),
                "list_e": ("LIST", {"forceInput": True}),
                "list_f": ("LIST", {"forceInput": True}),
            },
        }

    def combine_input_lists(self, separator, newline_char, **kwargs):
        lists = []
        for k in sorted(kwargs.keys()):
            if isinstance(kwargs[k], list):
                lists.append(kwargs[k])
        return (self.join_filtered_lists(separator, newline_char, *lists),)

    def join_filtered_lists(self, separator, newline_char, *lists) -> str:
        return newline_char.join(map(separator.join, self.get_filtered_product(*lists)))

    def get_filtered_product(self, *lists):
        return [filter(None, x) for x in itertools.product(*lists)]

    RETURN_NAMES = ("STRING",)
    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_input_lists"
    CATEGORY = "TextListProduct"
