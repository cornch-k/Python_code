n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    sum = 0
    for j in range(a, b+1):
        if j == 0:
            sum += 1
        elif j % 10 == 0:
            sum += 1
            if j % 100 == 0:
                sum += 1
                if j % 1000 == 0:
                    sum += 1
                    if j % 10000 == 0:
                        sum += 1
                        if j % 100000 == 0:
                            sum += 1
                            if j % 1000000 == 0:
                                sum += 1
    print(sum)