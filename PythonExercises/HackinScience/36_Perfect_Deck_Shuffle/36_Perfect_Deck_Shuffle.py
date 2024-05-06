def perfect_shuffle(deck: list, times: int):
    result = deck
    halfLen = len(result)//2
    for i in range(times):
        shuffle = []
        deckA = result[:halfLen]
        deckB = result[halfLen:]
        for num in range(halfLen):
            shuffle.append(deckA[num])
            shuffle.append(deckB[num])
        result = shuffle
    return result

print(perfect_shuffle(range(1024), 10))