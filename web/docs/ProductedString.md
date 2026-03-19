# ProductedString

Create multiple prompt combinations from several lists and return them as one multiline string.

## Inputs

- Multiple text list inputs
- `separator`: String inserted between combined items
- `max_results`: Maximum number of generated lines. `0` means unlimited.

## Behavior

- This is a shorthand node built on top of the text list product logic.
- It combines multiple lists instead of only two.
- The result is returned as a single string with line breaks, ready for downstream text-processing nodes.

## Usage

Use this node for general prompt pattern generation when you want one multiline block instead of list-style intermediate outputs.

