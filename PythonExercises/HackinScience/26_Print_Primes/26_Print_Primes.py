def is_prime(num):
    for i in range(2, num + 1):
        if (num % i == 0):
            if (num == i):
                return True
            else:
                return False
    return False

def print_primes(n):
    for i in range(2, n):
        if is_prime(i) == True:
            print(i)

print_primes(10)