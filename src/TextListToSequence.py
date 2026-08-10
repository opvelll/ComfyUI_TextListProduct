class TextListToSequence:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("LIST", {"forceInput": True}),
            },
        }

    def convert_to_sequence(self, text_list):
        if not isinstance(text_list, list):
            raise TypeError(
                "TextListToSequence expected a list, "
                f"got {type(text_list).__name__}."
            )

        if not text_list:
            raise ValueError(
                "TextListToSequence requires at least one item; "
                "ComfyUI cannot process an empty sequential list."
            )

        for index, item in enumerate(text_list):
            if not isinstance(item, str):
                raise TypeError(
                    "TextListToSequence expected a string at "
                    f"index {index}, got {type(item).__name__}."
                )

        return (text_list,)

    RETURN_NAMES = ("string",)
    RETURN_TYPES = ("STRING",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "convert_to_sequence"
    CATEGORY = "TextListProduct"
