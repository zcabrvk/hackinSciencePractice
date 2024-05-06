def multiples_of_three_and_five():
    result = 0
    for i in range(0, 1000):
        if (i % 3 == 0) or (i % 5 == 0):
            result += i
    return result

print(multiples_of_three_and_five())