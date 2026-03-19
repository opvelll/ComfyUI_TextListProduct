# Notes

- This plugin was reviewed and partially updated on 2026-03-20.
- `PromptPairConcat` was fixed so `separator` is respected in both clean and non-clean modes.
- `PromptPairConcat` now has `trailing_separator` with default `false`.
- Product-style nodes now support `max_results`.
- `max_results = 0` means unlimited. Positive values truncate output from the start of the generated cartesian product.

# Touched Areas

- [src/PromptPairConcat.py](C:\Users\segawa\ComfyUI_TextListProduct\src\PromptPairConcat.py)
- [src/BaseTextListProduct.py](C:\Users\segawa\ComfyUI_TextListProduct\src\BaseTextListProduct.py)
- [src/TextListProduct.py](C:\Users\segawa\ComfyUI_TextListProduct\src\TextListProduct.py)
- [src/TextListProductWithSingleA.py](C:\Users\segawa\ComfyUI_TextListProduct\src\TextListProductWithSingleA.py)
- [src/TextListProductWithSingleB.py](C:\Users\segawa\ComfyUI_TextListProduct\src\TextListProductWithSingleB.py)
- [src/TextListProductWithSingleBoth.py](C:\Users\segawa\ComfyUI_TextListProduct\src\TextListProductWithSingleBoth.py)
- [src/ProductedString.py](C:\Users\segawa\ComfyUI_TextListProduct\src\ProductedString.py)
- [tests/test_PromptPairConcat.py](C:\Users\segawa\ComfyUI_TextListProduct\tests\test_PromptPairConcat.py)
- [tests/test_ProductedString.py](C:\Users\segawa\ComfyUI_TextListProduct\tests\test_ProductedString.py)
- [tests/test_NodeRegistration.py](C:\Users\segawa\ComfyUI_TextListProduct\tests\test_NodeRegistration.py)

# Verification

- Run: `python -m unittest discover -s tests -v`
- Last known result after changes: 35 tests passed.

# Open Ideas

- A useful next node would likely be one of:
  - `TextListCartesianSize`
  - `TextListNormalize`
  - `TextTemplateFormat`
- If adding new product-like nodes, reuse `BaseTextListProduct`.
- If changing `PromptPairConcat` again, check README and tests together because old behavior was inconsistent.
