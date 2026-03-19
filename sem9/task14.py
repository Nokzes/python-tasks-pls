st = input()
st = list(st.split())
for i in range(len(st)):
    st[i] = int(st[i])

mx = st.index(max(st))
mn = st.index(min(st))

st[mx], st[mn] = st[mn], st[mx]

print(' '.join(map(str, st)))



