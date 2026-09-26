a = int(input())
count = 64

while a % 2 == 0:
    a //= 2
    count-= 1
print(count)