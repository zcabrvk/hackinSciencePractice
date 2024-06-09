def fibonacci(numbers: int):
    sum1 = 0
    sum2 = []
    for i in range(0, numbers):
        if i == 0:
            sum2.append(1)
        if i > 0:
            temp = sum2[i - 1]
            sum2.append(sum1 + temp)
            sum1 = temp
    return sum2