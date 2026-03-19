n = int(input())
otr = []
pl = []
nuli = []

for _ in range(n):
    a = int(input())
    if a < 0:
        otr.append(a)
    elif a == 0:
        nuli.append(0)
    else:
        pl.append(a)

print(f"{otr} \n{nuli} \n{pl}")

