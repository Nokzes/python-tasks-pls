st = input()
res = 0

for i in range(len(st)-1):
    if st[i] == st[i+1]:
        res += 1

print(res)



