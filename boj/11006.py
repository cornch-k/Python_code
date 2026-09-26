Num = int(input())
for i in range(Num):
    x, y = map(int, input().split())
    T = x - y
    U = x - (2 * T)
    print(U, T)