n = int(input())

first = 0
second = 0

for i in range(n):
    x =  int(input())
    if i == 0:
        first = x
    elif i == 1:
        if x >= first:
            second = first
            first = x
        else:
            second = x
    else:
        if x >= first:
            second = first
            first = x
        elif x > second and x < first:
            second = x

print(first, second)

