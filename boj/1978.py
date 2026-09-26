prime_count = 0

a = int(input())
prime_number = map(int, input().split())

for i in prime_number:
    overlap = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                overlap += 1
        if overlap == 0:
            prime_count += 1

print(prime_count)