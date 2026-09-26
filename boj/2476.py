n = int(input())
money_list = []
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2]:
        money_list.append(10000 + a[0]* 1000)
    elif a[0] == a[1] and a[0] != a[2]:
        money_list.append(1000 + a[0] * 100)
    elif a[0] == a[2] and a[0] != a[1]:
        money_list.append(1000 + a[0] * 100)
    elif a[1] == a[2] and a[0] != a[1]:
        money_list.append(1000 + a[1] * 100)
    else:
        money_list.append(max(a) * 100)
print(max(money_list))