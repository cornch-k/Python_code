NumSort = list(map(int, input().split()))
NumSort.sort()
for i in range(len(NumSort)):
    print(NumSort[i], end= ' ')