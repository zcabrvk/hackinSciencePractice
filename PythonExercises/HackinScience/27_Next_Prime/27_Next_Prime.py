import itertools
import sys


def is_prime(num):
    for i in range(2, num + 1):
        if (num % i == 0):
            if (num == i):
                return True
            else:
                return False
    return False

for i in itertools.count(start = 100000000, step=1):
    print("Checking if " + str(i) + " is prime")
    if is_prime(i):
        print(str(i) + " is prime")
        sys.exit()