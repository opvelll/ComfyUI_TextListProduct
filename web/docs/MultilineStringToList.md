# MultilineStringToList

Convert a multiline string into a `LIST` with one item per line.

## Inputs

- `text`: The multiline string to split
- `trim_whitespace`: Remove whitespace around each line; enabled by default
- `keep_empty_lines`: Keep empty lines as empty string items; disabled by default

## Behavior

- Supports LF, CRLF, and CR line endings.
- Empty input returns an empty list.
- A trailing line ending does not add an empty item.
- Lines that look like comments are kept as normal text.
- When trimming is enabled, whitespace-only lines become empty before empty-line filtering.

## Usage

Use this node to enter prompt candidates directly in one text box and connect the resulting list to any TextListProduct node.
