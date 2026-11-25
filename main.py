"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: a childhood
memory of grandma's kitchen, the smell of fresh rice, and a pot
lid rattling like a tiny drum. Standard library only.
"""

import os

MEMORY = (
    "Grandma's kitchen smelled of fresh rice and wood smoke, and I "
    "was small enough to hide under the table while she hummed and "
    "the pot lid rattled like a tiny drum."
)


def check_memory(text):
    """Check the memory against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 280 characters, not only
    white space, in a single sentence: one childhood memory that
    brings back a place, a time or a sensation. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("memory must not be only whitespace")
    if len(cleaned) > 280:
        raise ValueError(
            "memory is %d characters, over the 280 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("memory must be exactly one line")
    return cleaned


def memory_measure(text):
    """Measure the memory for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A memory too short to hold a place and a
    sensation, or one padded out to fill the cap instead of leaving
    the warm ache behind, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_memory(MEMORY)
    measure = memory_measure(text)
    if measure["words"] < 5:
        raise ValueError("memory is too short to hold a place")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
