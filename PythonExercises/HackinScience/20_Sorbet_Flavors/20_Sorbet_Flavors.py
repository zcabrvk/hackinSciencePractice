FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

parsedFlavors = set()

for i in FLAVORS:
    for j in FLAVORS:
        if (i not in parsedFlavors) and (j not in parsedFlavors) and (i != j):
            print(i + ", " + j)
    parsedFlavors.add(i)