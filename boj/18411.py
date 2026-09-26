a, b, c = map(int, input().split())
if a + b == max(a+b, b+c, a+c):
    print(a+b)
elif b + c == max(a+b, b+c, a+c):
    print(b+c)
elif a + c == max(a+b, b+c, a+c):
    print(a+c)