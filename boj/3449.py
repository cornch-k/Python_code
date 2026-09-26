import sys

n = int(sys.stdin.readline())
for i in range(n):
    count = 0
    first = sys.stdin.readline()
    second = sys.stdin.readline()
    for j in range(len(first)):
        if first[j] == second[j]:
            continue
        else:
            count +=1
    print("Hamming distance is %d." % count)