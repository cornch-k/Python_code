listfreq = []

A, B = map(int, input().split())
N = int(input())

for i in range(N):
    listfreq.append(abs(int(input()) - B))
print(min(abs(A - B), min(listfreq) + 1))