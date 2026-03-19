n = int(input())
counter = 0

for _ in range(n):
    a = input()
    if a.count("11") >= 3:
        counter += 1

print(counter)


