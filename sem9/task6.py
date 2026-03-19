n = int(input())
res = []

for i in range(n):
    a = input()
    if i % 2 == 0:
        res.append(a)

print(res)



'''
for i in range(n):
    a = input()
    res.append(a)

del res[::2]
print(res)
'''

