def is_one_away(word1: str, word2: str) -> bool:
    mis = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mis += 1
                if mis > 1:
                    return False
        return True
    else:
        return False

print(is_one_away(input(), input()))

