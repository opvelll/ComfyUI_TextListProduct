from .src.TextListProduct import TextListProduct
from .src.TextListProductWithSingleA import TextListProductWithSingleA
from .src.TextListProductWithSingleB import TextListProductWithSingleB
from .src.TextListProductWithSingleBoth import TextListProductWithSingleBoth
from .src.ProductedString import ProductedString
from .src.MultilineStringToList import MultilineStringToList
from .src.StringsToList import StringsToList
from .src.TextListToSequence import TextListToSequence

from .src.PromptPairConcat import PromptPairConcat

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
    "TextListProduct": TextListProduct,
    "TextListProductWithSingleA": TextListProductWithSingleA,
    "TextListProductWithSingleB": TextListProductWithSingleB,
    "TextListProductWithSingleBoth": TextListProductWithSingleBoth,
    "ProductedString": ProductedString,
    "PromptPairConcat": PromptPairConcat,
    "MultilineStringToList": MultilineStringToList,
    "StringsToList": StringsToList,
    "TextListToSequence": TextListToSequence,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextListProduct": "Text List Product",
    "TextListProductWithSingleA": "Text List Product With Single A",
    "TextListProductWithSingleB": "Text List Product With Single B",
    "TextListProductWithSingleBoth": "Text List Product With Single Both",
    "ProductedString": "Producted String",
    "PromptPairConcat": "Prompt Pair Concat",
    "MultilineStringToList": "Multiline String to List",
    "StringsToList": "Strings to List",
    "TextListToSequence": "Text List to Sequence",
}
