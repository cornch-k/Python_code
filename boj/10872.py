import time


def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

n = int(input())
start= time.time()

print(factorial(n))
end = time.time()
print(end - start)