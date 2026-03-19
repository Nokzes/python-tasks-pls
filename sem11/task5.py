def get_days(month: int) -> int:
    lst30 = [4, 6, 9, 11]
    if month in lst30:
        return 30
    elif month == 2:
        return 28
    else:
        return 31

a = get_days(int(input()))
print(a)


