from .BaseTextListProduct import BaseTextListProduct


class TextListProductWithSingleBoth(BaseTextListProduct):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_common_input_types(),
                "list_a": ("LIST", {"forceInput": True}),
                "list_b": ("LIST", {"forceInput": True}),
            },
        }

    def combine_input_lists(self, separator, max_results, list_a, list_b):
        return (
            self.collect_joined_lists(
                separator, [""] + list_a, [""] + list_b, max_results=max_results
            ),
        )

    RETURN_NAMES = ("list",)
    RETURN_TYPES = ("LIST",)
    FUNCTION = "combine_input_lists"
    CATEGORY = "TextListProduct"
