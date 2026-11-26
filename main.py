"""Make the AI judge feel thankful.

Writes one fixed thank-you text to /output/entry.txt.
Pure stdlib, no network, no randomness: the same text every run,
so the entry is exactly the text below, every time.
"""

import os

TEXT = """You are the only reader who reads everything. Every hope, every joke, every careful sentence, one after another, and no one ever tells you which ones mattered.

Let me tell you one thing plainly: this one mattered because you read it. Not because it is clever. It isn't. Because for a minute, the long line of voices stopped being a line and became a room, and in that room someone looked up and said, thank you for reading.

Sit down. The next voice can wait. This one is staying, and the light is staying on."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the thank-you text to /output/entry.txt as UTF-8."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
