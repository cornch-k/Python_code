import sys

n = int(sys.stdin.readline())
for i in range(n):
    b = list(map(int, sys.stdin.readline().split()))
    print(sum(b))