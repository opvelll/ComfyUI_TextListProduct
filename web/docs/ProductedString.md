# ProductedString

Create multiple prompt combinations from several lists and return both a multiline string and the underlying result list.

## Inputs

- Multiple text list inputs
- `separator`: String inserted between combined items
- `max_results`: Maximum number of generated lines. `0` means unlimited.
- `newline_char`: String inserted between results in the multiline `STRING` output

## Outputs

- `STRING`: Every combination joined with `newline_char`
- `list`: The same combinations as one custom `LIST` value

## Behavior

- This is a shorthand node built on top of the text list product logic.
- It combines multiple lists instead of only two.
- Both outputs contain the same combinations in the same order and respect `max_results`.
- `newline_char` affects only the `STRING` output; it is not added to the items in `list`.
- With no connected list inputs, the node returns an empty string and an empty list.

## Usage

Use `STRING` when the complete result should be displayed or saved as text. Connect `list` to `Text List to Sequence` when each combination should be processed separately by downstream ComfyUI nodes.
