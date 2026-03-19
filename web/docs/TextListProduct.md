# TextListProduct

Create a cartesian product from two text lists and join each pair with the selected separator.

## Inputs

- `text_a`: First multiline text list
- `text_b`: Second multiline text list
- `separator`: String inserted between paired items
- `max_results`: Maximum number of generated combinations. `0` means unlimited.

## Behavior

- Each non-empty line is treated as one item in the list.
- The node combines every item from `text_a` with every item from `text_b`.
- Output order follows normal cartesian product order.

## Usage

Use this node when you want to build prompt variations such as:

- subject x hairstyle
- subject x location
- pose x camera angle

It works well with nodes that consume multiline text, such as line loaders and prompt list nodes.

