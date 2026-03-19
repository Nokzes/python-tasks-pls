st = input()
st = st.split()
a = len(st)
counter = 0

for i in range(a):
    for j in range(i+1, a):
#        print(i,st[i], j, st[j], st[i] == st[j])
        if st[i] == st[j]:
            counte+= 1

print(counter)


