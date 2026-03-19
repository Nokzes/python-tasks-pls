def find_all(target: str, symbol: str) -> list:
    res = []
    for i in range(len(target)):
        if target[i] == symbol:
            res.append(i)

    return res


a = find_all(input(), input())
print(a)

