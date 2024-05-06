def flatten(lists: list):
    result = []
    for element in lists:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result


print(flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]))