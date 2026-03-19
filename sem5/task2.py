word = ''
ans = 0
flag = True

while flag:
    word = input()
    ans += 1
    if (word == 'стоп') or (word == 'хватит') or (word == 'достаточно'):
        flag = False
        ans -= 1

print(ans)


