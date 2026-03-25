def solve(st: str) -> str:
    res = st.strip()
    if len(st) % 2 == 1:
        res = res.lower()
    else:
        res = res.upper()
    return res

print(solve("hello"))
print(solve("PyThon"))



