import sys
a = int(sys.stdin.readline())
b = set()
for i in range(a):
    number = int(sys.stdin.readline())
    b.add(number)

for i in sorted(b, reverse= True):
    print(i)