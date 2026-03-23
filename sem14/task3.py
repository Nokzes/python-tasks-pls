def my_func(st: str):
    st = st.split(',')
    # st = '1,2,3,4'
    for i in range(len(st)):
        st[i] = int(st[i])
    
    if len(st) == 4:
        if (st[0] + 1 == st[1]) and (st[1] + 1 == st[2]) and (st[2] + 1 == st[3]):
            a = st[0] * st[1] * st[2] * st[3] + 1
            b = a**0.5
            return [a, b]
        else:
            return "not consecutive"
    else:
        return "invalid input"

print(my_func('1,2,3,4'))
print(my_func('1,3,4,5'))
print(my_func('123124'))


