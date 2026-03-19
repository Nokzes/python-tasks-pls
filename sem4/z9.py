n = int(input())
z = []
ans = []
for _ in range(n):
    a = int(input())
    z.append(a)

ans.append(max(z))
z.remove(max(z))
ans.append(max(z))

for i in ans:
    print(i)


