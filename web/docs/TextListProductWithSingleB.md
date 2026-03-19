# TextListProductWithSingleB

Variant of `TextListProduct` that also keeps single items from list B.

## Inputs

- `text_a`: First multiline text list
- `text_b`: Second multiline text list
- `separator`: String inserted between paired items
- `max_results`: Maximum number of generated combinations. `0` means unlimited.

## Behavior

- Works like `TextListProduct`.
- Also includes outputs where items from `text_b` are used by themselves.
- Useful when the second list should remain optional.

## Usage

Use this when you want outputs such as:

- `blonde_hair`
- `1girl, blonde_hair`
- `1boy, blonde_hair`

without manually inserting empty values into the first list.

