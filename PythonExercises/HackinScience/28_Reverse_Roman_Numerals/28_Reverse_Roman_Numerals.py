def from_roman_numeral(numeral):
    result = 0

    if "CM" in numeral:
        result += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        result += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        result += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        result += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        result += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        result += 4
        numeral = numeral.replace("IV", "")

    for c in numeral:
        if c == "M":
            result += 1000
        if c == "C":
            result += 100
        if c == "D":
            result += 500
        if c == "X":
            result += 10
        if c == "L":
            result += 50
        if c == "I":
            result += 1
        if c == "V":
            result += 5

    return result

print(from_roman_numeral("DCCXCII"))
print(from_roman_numeral("DXXXI"))
print(from_roman_numeral("LXXXIV"))