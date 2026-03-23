numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

def is_positive(num: int) -> bool:
    if num >= 0:
        return True
    else:
        return False

def count_positive(nums: list) -> int:
    res = 0
    for c in nums:
        if is_positive(c):
            res += 1
    return res

def count_negative(nums: list) -> int:
    res = len(nums) - count_positive(nums)
    return res

print(f"Количество положительных чисел = {count_positive(numbers)}")
print(f"Количество отрицательных чисел = {count_negative(numbers)}")

