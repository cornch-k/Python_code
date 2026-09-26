import sys

n = sys.stdin.readline().split()

for i in range(len(n)):
    for j in range(1, len(n)):
        if n[j] < n[j-1]:
            
            n[j], n[j-1] = n[j-1], n[j]
            print(" ".join(n))