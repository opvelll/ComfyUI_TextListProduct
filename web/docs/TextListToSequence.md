# TextListToSequence

Convert a custom text `LIST` into ComfyUI's sequential `STRING` output.

## Inputs

- `text_list`: A connected `LIST` containing one or more strings

## Output

- `string`: A sequential `STRING` output. A downstream node is executed once for each item.

## Behavior

- Preserves item order and empty string items.
- Rejects an empty list with a clear error because ComfyUI cannot safely process an empty sequential list.
- Rejects non-string items and reports the invalid item's index.
- Does not enable `INPUT_IS_LIST`; the input remains this package's custom list container.

## Usage

For sequential prompt processing, connect:

`TextListProduct → Text List to Sequence → CLIP Text Encode`

Use the regular `LIST` output directly when another TextListProduct node needs the whole list as one value. Add this conversion only at the point where downstream nodes should run once per string.
