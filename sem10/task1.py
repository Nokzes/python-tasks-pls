st = input()
res = 0

st = st.split(".")

for i in range(len(st)):
    st[i] = int(st[i])

for c in st:
    if c >= 0 and c < 256:
        res += 1

if res == 4:
    print("YES")
else:
    print("NO")




