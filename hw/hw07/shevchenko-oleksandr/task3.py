"""Count the occurrences of each character in a string."""

from collections import Counter


def count_chars(text: str) -> dict[str, int]:
    """Return a dictionary mapping each character to its count."""
    return dict(Counter(text))


if __name__ == "__main__":
    print(count_chars("hello"))
