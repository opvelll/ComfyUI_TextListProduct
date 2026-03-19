# TextListProductWithSingleBoth

Variant of `TextListProduct` that keeps single items from both lists in addition to full combinations.

## Inputs

- `text_a`: First multiline text list
- `text_b`: Second multiline text list
- `separator`: String inserted between paired items
- `max_results`: Maximum number of generated combinations. `0` means unlimited.

## Behavior

- Generates the normal cartesian product.
- Also includes single entries from list A.
- Also includes single entries from list B.

## Usage

Use this when both sides should be optional and you still want the combined forms.

