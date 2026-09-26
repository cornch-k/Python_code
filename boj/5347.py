import math

n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    print(f"{math.lcm(num1, num2)}")