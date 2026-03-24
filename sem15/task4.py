def hackers_def(hackers: list, security_level: int, increase: int) -> int:
    res = 0
    for c in hackers:
        if c <= security_level:
            security_level += increase
        else:
            res += 1

    return res

print(hackers_def([5, 4, 2, 7, 8], 3, 1))




