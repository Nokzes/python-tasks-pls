n = int(input())
mx = 0

for i in range(n):
    x = int(input())
    if i == 0:
        mx = x
    if x > mx:
        mx = x
print(mx)

