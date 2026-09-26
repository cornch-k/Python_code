n = int(input())
for i in range(n):
    sentence = list(input().split())
    for j in sentence:
        print(j[::-1], end=" ")
    print()