def is_prime(num):
    for i in range(2, num + 1):
        if (num % i == 0):
            if (num == i):
                return True
            else:
                return False
    return False

def sum_of_prime_below(n):
    result = 0
    for i in range(2, n):
        if is_prime(i) == True:
            result+=i
    return result

print(sum_of_prime_below(10))