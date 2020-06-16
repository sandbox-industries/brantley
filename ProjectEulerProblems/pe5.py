to_num = 20
primes = []
for x in range(2, to_num):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
            break
    if prime:
        new_prime = x
        while True:
            if new_prime * x > to_num:
                break
            else:
                new_prime *= x
        primes.append(new_prime)
answer = 1
for x in primes:
    answer *= x
print(answer)
