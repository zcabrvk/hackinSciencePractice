euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]

def how_to_pay(amount: int, currency: list):
    currency.sort(reverse=True)
    result = dict()
    remaining = amount
    while remaining != 0:
        note = next((x for x in currency if (x - remaining) <= 0), None)
        noteCount = result.get(note, 0)
        noteCount = noteCount + 1
        result[note] = noteCount
        remaining = remaining - note
    return result

print(how_to_pay(500, euro))
print(how_to_pay(10, euro))
print(how_to_pay(123, euro))
print(how_to_pay(8, euro))
print(how_to_pay(100, [50,20,10,5]))
