import sys

lists = []
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    lists.append(a)
lists.sort()
for j in lists:
    print(j)