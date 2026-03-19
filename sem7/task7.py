st = input()
res = ''
counter = 0

for c in st:
    a = st.count(c)
    if a >= counter:
        res = c
        counter = a

print(res)


