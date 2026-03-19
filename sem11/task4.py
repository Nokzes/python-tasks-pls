def sum(lst: list) -> int:
    res = 0
    for c in lst:
        res += c
    return res

def sr(lst: list) -> float:
    res = sum(lst) / len(lst)
    return res

lst = [10, 24, 124, 2]
a = sum(lst)
b = sr(lst)

print(a, b)

