a = int(input())
for i in range(a):
    count = 0
    b = input()
    for j in range(0, 10):
        if str(j) in b:
            count += 1
        else:
            continue
    print(count)