import string
from collections import Counter

PUNC = string.punctuation  # pull in pre-made punctuation list


def clean_words(input_text: str) -> list[str]:
    # 1. split each word separately
    words = input_text.lower().split()

    # 2. loop through each word, strip punctuation, `if w` for edge cases
    stripped = [w.strip(PUNC) for w in words]
    new_words = [w for w in stripped if w]

    return new_words


def count_words(text: str) -> dict[str, int]:
    words = clean_words(text)
    # 3. count words
    counted = {}
    for w in words:
        counted[w] = counted.get(w, 0) + 1

    return counted


def count_words_counter(text: str) -> dict[str, int]:
    # 3. count words alternate
    words = clean_words(text)

    return dict(Counter(words))


# run it
if __name__ == "__main__":

    text = "The cat sat. The cat ran!"

    print("...testing equivalency...")
    assert count_words(text) == count_words_counter(text)  # first check equivalency
    print("Equivalency check passed.")

    print("...testing functions...")
    assert count_words(text) == {'the': 2, 'cat': 2, 'sat': 1, 'ran': 1}
    assert count_words_counter(text) == {'the': 2, 'cat': 2, 'sat': 1, 'ran': 1}
    print("Function test passed.")

    print("...testing edge cases...")
    for fn in (count_words, count_words_counter):
        assert fn("the the the") == {"the": 3}
        assert fn("a - b") == {"a": 1, "b": 1}
    print("Edge cases passed.")
