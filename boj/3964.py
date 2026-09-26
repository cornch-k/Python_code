import math


def factorials():
    a, b = map(int, input().split()) #a, b를 입력
    a_fct = math.factorial(a)
    count = 0
    while True:
        if a_fct % b != 0:
            break
        else:
            count += 1
            a_fct //= b
    return count


n = int(input())
for i in range(n):
    print(factorials())