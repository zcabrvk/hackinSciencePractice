def sum_of_even(start, stop):
    result = 0
    for i in range(start, stop + 1):
        if i & 2 == 0:
            result += i
    return result

print(sum_of_even(0, 100))