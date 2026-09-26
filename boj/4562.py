a =int(input())

for i in range(a):
    b, c = map(int, input().split())
    if b >= c:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")