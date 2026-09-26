a, b = map(int, input().split())
result = int((1 + a) * a / 2)

for i in range(a + 1, b + 1):
    result *= int ((i * (1 + i)) / 2)

print(result % 14579)
#% 쓰는 문제