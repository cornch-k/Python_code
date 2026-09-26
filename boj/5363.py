a = int(input())

for i in range(a):
    b = list(map(str, input().split()))
    b += b[0:2]
    del b[0:2]
    
    for j in b:
        print(j, end=' ')