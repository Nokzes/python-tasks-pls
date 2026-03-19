st = 0
ans = []

while (st % 7 == 0):
    st = int(input())
    ans.append(st)
del ans[-1]
for i in ans:
    print(i)





