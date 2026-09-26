n = int(input())
for i in range(n):
    num = list(map(int, input().split()))
    num.sort()
    print(num[-3])