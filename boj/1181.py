import sys
a = int(sys.stdin.readline())
l = set()

for i in range(a):
    b = input()
    l.add(b)

l = list(l)
l.sort(key=len)

for i in l:
    print(i)