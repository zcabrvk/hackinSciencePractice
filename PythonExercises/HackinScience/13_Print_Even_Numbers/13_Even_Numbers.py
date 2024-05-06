def print_even_numbers(start, stop):
    for i in range(start, stop + 1):
        if i % 2 == 0:
            print(str(i) + " is even")


print_even_numbers(0, 20)