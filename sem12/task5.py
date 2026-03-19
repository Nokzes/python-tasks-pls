all_unique(text: str) -> bool:
    for i in len(text):
        if text.count(text[i]) > 1:
            return False
        else:
            return True

a = all_unique(input())
print(a)
