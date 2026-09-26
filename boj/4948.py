def ers(b):
    prime_index = [False,False] + [True]*(b-1)
    global primes
    primes = []

    for i in range(2, 2 * b + 1):
        if prime_index[i]:
            primes.append(i)
        for j in range(2*i, b+1, i):
            prime_index[j] = False
    return primes


while True:
    b = int(input())
    real_prime_list = list()
    if b == 0:
        break
    ers(b)
    for i in range(len(ers(b))):
        if primes[i] < b:
            continue
        else:
            real_prime_list.append(primes[i])
    print(len(real_prime_list))



# real_prime_list = list()
# for i in range(len(primes)):
    # if primes[i] < b:
        # continue
    # else:
        # real_prime_list.append(primes[i])
# print(len(real_prime_list))
