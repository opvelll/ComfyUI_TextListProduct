from .BaseTextListProduct import BaseTextListProduct


class ProductedString(BaseTextListProduct):
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

    def combine_input_lists(self, separator, newline_char, **kwargs) -> str:
        # list_aから順に、接続されているものだけをリストにする
        lists = []
        for k in sorted(kwargs.keys()):
            if isinstance(kwargs[k], list):
                lists.append(kwargs[k])
        return (newline_char.join(self.join_filtered_lists(separator, *lists)),)

    RETURN_NAMES = ("STRING",)
    RETURN_TYPES = ("STRING",)
    FUNCTION = "combine_input_lists"
    CATEGORY = "TextListProduct"
