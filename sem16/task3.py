def my_func(st: str):
    nums =  '0123456789,'
    for c in st:
        if c not in nums:
            return "invalid input"
    st = st.split(',')
    for i in range(len(st)):
        st[i] = int(st[i])
    if (st[0] + 1 == st[1]) and (st[1] + 1 == st[2]):
        res = st[0] + st[1] + st[2]
        return res
    else:
        return "unexpected error"

print(my_func('0,1,2'))
print(my_func('1,2,4'))
print(my_func('aa,1,2'))



