def count_words_by_length(text: str, n: int) -> int:
    counter = 0
    text = text.split()
    for c in text:
        if len(c) == n:
            counter += 1

    return counter

print(count_words_by_length(input(), int(input)))
