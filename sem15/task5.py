def my_func(arr: list) -> list:
    res = []
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    vr_res = 0

    for i in range(len(arr)):
        vr_res = 0
        for j in arr[i]:
            vr_res += alphabet.index(j)
        res.append(vr_res * (i+1))
    return res

print(my_func(['abc', 'a b  c', 'a', 'zxca']))


