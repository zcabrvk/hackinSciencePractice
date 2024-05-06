def is_prime(num):
    for i in range(2, num + 1):
        if (num % i == 0):
            if (num == i):
                return True
            else:
                return False
    return False


print(is_prime(2))
print(is_prime(5))
print(is_prime(29))
print(is_prime(32))
print(is_prime(97))