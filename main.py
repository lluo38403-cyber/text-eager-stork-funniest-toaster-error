"""The Funniest Toaster Error Message — make.fun entry.

Writes the one line a kitchen toaster shows its owner when something
goes wrong to /output/entry.txt. The toaster has lost the bread, swears
it toasted it, and begs not to be unplugged.
"""

import os

ENTRY = (
    "ERROR 404: Bread not found. I toasted it, I swear. "
    "Please do not unplug me."
)

MAX_CHARS = 120


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
