"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard for an ordinary office object,
recast as an ancient artifact, to entry.txt in the output directory.
"""

import os

ENTRY = (
    "Stapler, c. 1998. Forged steel. Instrument of the Binding Rite: "
    "two sheets joined for eternity, no divorce permitted. "
    "Gift of Accounts Payable."
)

MAX_CHARS = 180


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 180 characters, and a
    # single line. Validate before writing so a bad entry never ships.
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry text is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} cap"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one trailing newline, written as UTF-8, every run.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
