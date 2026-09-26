N, L = map(int, input().split())
fruit = list(map(int ,input().split()))
fruit.sort()

for j in fruit:
    if j > L:
        break
    else:
        L += 1
print(L)