def sumOfDigits(num):
    if num >= 1:
        return (num % 10 + sumOfDigits(num // 10))
    else:
        return 0

a = int(input())
sumOfDigits(a)