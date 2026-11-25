"""The best meal I ever had, as a single sentence.

The program validates the sentence (one line, 1-200 characters) and
writes it, with no trailing newline, to /output/entry.txt.

The sentence is kept as one constant so the file stays trivial to audit:
what you read in ENTRY is exactly what lands in the output file.
"""

import os

ENTRY = (
    "At my grandmother's kitchen table, rain tapping the tin roof, I ate her "
    "beef rendang off a chipped blue plate, the coconut steam curling up as "
    "she laughed and spooned me more."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry sentence meets the bounty rules."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    return text


def self_test():
    """Validate the sentence and report its length."""
    validate(ENTRY)
    print("entry OK: %d characters" % len(ENTRY))


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
