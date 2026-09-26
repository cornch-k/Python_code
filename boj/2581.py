a = int(input())
b = int(input())
prime_index = [False,False] + [True]*(b-1)
primes=[]

for i in range(2,b+1):
  if prime_index[i]:
    primes.append(i)
    for j in range(2*i, b+1, i):
        prime_index[j] = False

# 우리가 쓸 값: primes(list)
real_prime_list = list()
for i in range(len(primes)):
    if primes[i] < a:
        continue
    else:
        real_prime_list.append(primes[i])

print(f"{sum(real_prime_list)}\n{real_prime_list[0]}" if len(real_prime_list) > 0 else -1)