'''
a = int(input())
b = int(input())

c = 3 * ((a + b)**3) + 275 * (b**2) - 127 * a - 41

print(c)
'''

'''
a = int(input())
print(a-1, a+1)
'''
'''
a = int(input())
b = int(input())
print(f"{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}")
'''

'''
x = int(input())
print(x, 2*x, 3*x, 4*x, 5*x, sep="---")
'''

'''
a = int(input())
print(a//100)
'''

'''
a = int(input())
b = int(input())
print(f"{b // a} \n{b % a}")
'''

'''
a = int(input())
print((a-1)//4+1)
'''

x = int(input()) # 123
a = str(x // 100)
b = str((x // 10) % 10)
c = str(x % 10)
print(a+b+c)
print(a+c+b)
print(b+a+c)
print(b+c+a)
print(c+a+b)
print(c+b+a)



