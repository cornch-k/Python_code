N, K = map(int, input().split())
count = 0
ao, aka, shiro = list(), list(), list()
for i in range(1, N + 1):
    ao.append(i)
    aka.append(i)
    shiro.append(i)

for i in ao:
    for j in aka:
        k = K - i - j
        if k > 0 and k <= N:
            count += 1

print(count)
