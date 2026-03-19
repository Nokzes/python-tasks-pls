num = 4
ans = 0
flag = True
while flag:
    num = int(input())
    if num == 5:
        ans += 1
    elif num > 5:
        flag = False
    elif num < 1:
        flag = False

print(ans)




