def sortxy():
    x = list()
    y = list()

    n = int(input())
    
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)