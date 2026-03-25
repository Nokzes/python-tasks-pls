def leg_func(lst: list) -> list:
    for c in lst:
        if c < 0:
            lst.remove(c)

    return lst

print(leg_func([1, 2, 5, -7, 1]))


