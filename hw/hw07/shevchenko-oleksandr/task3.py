from collections import Counter


def count_chars(text: str) -> dict[str, int]:
    return dict(Counter(text))


if __name__ == "__main__":
    print(count_chars("hello"))
