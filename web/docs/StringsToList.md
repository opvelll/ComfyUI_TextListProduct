# StringsToList

Collect up to seven connected strings into one `LIST`.

## Inputs

- `text_a` through `text_g`: Optional connected string inputs

## Behavior

- Connected inputs are returned in alphabetical input order.
- Unconnected inputs are skipped.
- Connected empty strings are preserved.
- If no inputs are connected, the node returns an empty list.

## Usage

Use this node when prompt candidates come from separate string-producing nodes. It replaces the list-building role of WAS Node Suite's Text List node without requiring WAS Node Suite.
