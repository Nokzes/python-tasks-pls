def is_zero(num: int) -> bool:
    if num == 0:
        return True
    else:
        return False

def count_zeros(numbers: str) -> int:
    res = 0
    numbers = numbers.split()
    for c in numbers:
        if is_zero(int(c)):
            res += 1
    return res

def count_non_zeros(numbers: str) -> int:
    res = 0
    numbers = numbers.split()
    for c in numbers:
        if is_zero(int(c)) == False:
            res += 1
    return res

def result_func(numbers: str):
    print(count_zeros(numbers))
    print(count_non_zeros(numbers))


result_func('12 0 0 23 -1')



