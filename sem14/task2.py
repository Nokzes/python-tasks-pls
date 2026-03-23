st = input()
def solve(st):
    res = ''
    cou_up = 0
    cou_lo = 0
    for c in st:
        if c.isupper():
            cou_up += 1
        elif c.islower():
            cou_lo += 1

    if (cou_up > cou_lo):
        for c in st:
            if c.isupper():
                res += c
            else:
                res += c.upper()
    else:
        for c in st:
            if c.islower():
                res += c
            else:
                res += c.lower()
    return res

print(solve(st))


