def is_password_good(password: str) -> bool:
    if1 = 0
    if2 = 0
    if3 = 0
    if4 = 0
    if len(password) >= 8:
        if4 = 1
    for c in password:
        if if1 == 0:
            if c.isupper():
                if1 = 1
                continue 
        elif if2 == 0:
            if c.istitle():
                if2 = 1
                continue
        elif if3 == 0:
            if c.isdigit():
                if3 = 1

        if if1 + if2 + if3+ if4 == 4:
            return True
        else:
            return False


a = is_password_good(input())
print(a)
