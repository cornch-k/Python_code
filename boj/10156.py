a, b, c = map(int, input().split())
d = a * b

if c - d >= 0:
    print(0)
else:
    print(d - c)