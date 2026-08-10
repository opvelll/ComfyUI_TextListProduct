class MultilineStringToList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": (
                    "STRING",
                    {
                        "default": "",
                        "multiline": True,
                        "dynamicPrompts": False,
                    },
                ),
                "trim_whitespace": ("BOOLEAN", {"default": True}),
                "keep_empty_lines": ("BOOLEAN", {"default": False}),
            },
        }

    def convert_to_list(self, text, trim_whitespace=True, keep_empty_lines=False):
        lines = text.splitlines()

        if trim_whitespace:
            lines = [line.strip() for line in lines]

        if not keep_empty_lines:
            lines = [line for line in lines if line != ""]

        return (lines,)

    RETURN_NAMES = ("list",)
    RETURN_TYPES = ("LIST",)
    FUNCTION = "convert_to_list"
    CATEGORY = "TextListProduct"
