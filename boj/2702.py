import math

a = int(input())
for i in range(a):
    num1, num2 = map(int, input().split())
    print(f"{math.lcm(num1, num2)} {math.gcd(num1, num2)}")