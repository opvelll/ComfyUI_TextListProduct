class StringsToList:
    INPUT_NAMES = tuple(f"text_{suffix}" for suffix in "abcdefg")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                name: ("STRING", {"forceInput": True}) for name in cls.INPUT_NAMES
            },
        }

    def collect_strings(self, **kwargs):
        strings = [
            kwargs[name]
            for name in self.INPUT_NAMES
            if name in kwargs and isinstance(kwargs[name], str)
        ]
        return (strings,)

    RETURN_NAMES = ("list",)
    RETURN_TYPES = ("LIST",)
    FUNCTION = "collect_strings"
    CATEGORY = "TextListProduct"
