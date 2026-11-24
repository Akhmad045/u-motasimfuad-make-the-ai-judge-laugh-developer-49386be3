"""Write one funny developer excuse to /output/entry.txt (no trailing newline).

Validation guard: the entry must be a single line of 1-200 characters with
no surrounding whitespace. An invalid entry raises instead of writing.
"""

import os

ENTRY = "My code worked perfectly until a user followed the instructions in the ticket."


def validate(entry: str) -> None:
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if entry != entry.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
