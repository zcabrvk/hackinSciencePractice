import unicodedata

result = ""

for i in range(0, 230000):
    name = unicodedata.name(chr(i), '')
    if 'HEART' in name:
        result += unicodedata.lookup(name)

print(result)