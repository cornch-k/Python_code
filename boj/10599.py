while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    else:
        print(c - b, d - a)