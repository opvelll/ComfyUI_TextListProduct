# TextListProductWithSingleA

Variant of `TextListProduct` that also keeps single items from list A.

## Inputs

- `text_a`: First multiline text list
- `text_b`: Second multiline text list
- `separator`: String inserted between paired items
- `max_results`: Maximum number of generated combinations. `0` means unlimited.

## Behavior

- Works like `TextListProduct`.
- Also includes outputs where items from `text_a` are used by themselves.
- Useful when one side should be optional.

## Usage

Use this when you want outputs such as:

- `1girl`
- `1girl, blonde_hair`
- `1girl, crown`

without manually adding blank lines to list B or rewriting prompts.

