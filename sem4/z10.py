n = int(input())
z = [1, 1]
answer = ""
if n == 1:
    print(1)
elif n == 2:
    print("1 1")
else:
    for _ in range(n-2):
        z.append(z[-1]+z[-2])
    for i in z:
        answer = f"{answer} {i}"
    answer = answer[1:]
    print(answer)



