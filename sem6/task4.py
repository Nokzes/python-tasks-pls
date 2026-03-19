st = input()
res1 = 0
res2 = 0


for c in st:
    if c == "+":
        res1 += 1
    elif c == "*":
        res2 += 1

print(f"Символ + встречается {res1} раз\nСимвол * встречается {res2} раз")


