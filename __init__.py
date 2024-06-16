
from .TextListProduct import TextListProduct
from .TextListProductWithSingleA import TextListProductWithSingleA
from .TextListProductWithSingleB import TextListProductWithSingleB
from .TextListProductWithSingleBoth import TextListProductWithSingleBoth
from .ProductedString import ProductedString

NODE_CLASS_MAPPINGS = {
    "TextListProduct": TextListProduct,
    "TextListProductWithSingleA": TextListProductWithSingleA,
    "TextListProductWithSingleB": TextListProductWithSingleB,
    "TextListProductWithSingleBoth": TextListProductWithSingleBoth,
    "ProductedString": ProductedString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextListProduct": "Text List Product",
    "TextListProductWithSingleA": "Text List Product With Single A",
    "TextListProductWithSingleB": "Text List Product With Single B",
    "TextListProductWithSingleBoth": "Text List Product With Single Both",
    "ProductedString": "Producted String",
}
