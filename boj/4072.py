while True:
    a = list(map(str, input().split()))
    if a[0] == a[-1] == '#':
        break

    for i in a:
        print(i[::-1], end = " ")