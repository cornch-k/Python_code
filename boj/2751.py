import sys

a = int(sys.stdin.readline())
b = []
for i in range(a):
    c = int(sys.stdin.readline())
    b.append(c)
b = set(b)
b = sorted(list(b))
for i in b:
    print(i)