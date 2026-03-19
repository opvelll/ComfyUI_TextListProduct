# PromptPairConcat

Concatenate two prompt lists element by element, similar to `zip`.

## Inputs

- `text_a`: First multiline text list
- `text_b`: Second multiline text list
- `separator`: String inserted between each pair
- `isClean`: Trim whitespace and clean duplicated separators before joining
- `trailing_separator`: Append the separator at the end of each output item

## Behavior

- Pairs the first line of A with the first line of B, the second with the second, and so on.
- Does not create a cartesian product.
- Useful when both lists already have matching structure.

## Usage

This node is useful for workflows where prompt fragments are prepared in parallel and should be recombined in order.
