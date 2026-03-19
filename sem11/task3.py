def print_case_counts(s: str):
    count_up = 0
    count_down = 0

    for c in s:
        if c.isupper():
            count_up += 1
        elif c.islower():
            count_down += 1
    
    print(f"Букв в верхнем регистре: {count_up}")
    print(f"Букв в нижнем регистре: {count_down}")


print_case_counts(input())
