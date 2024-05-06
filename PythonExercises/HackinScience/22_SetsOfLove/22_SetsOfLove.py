districts_in_paris = {"Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ", "Ⅹ", "ⅩⅠ", "ⅩⅡ", "ⅩⅢ", "ⅩⅣ", "ⅩⅤ", "ⅩⅥ", "ⅩⅦ", "ⅩⅧ", "ⅩⅠⅩ", "ⅩⅩ"}

# Exercise 1
def love_meet(bobPaths, alicePaths):
    bobSet = set(bobPaths)
    aliceSet = set(alicePaths)
    print(bobSet & aliceSet)


bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
alice = ['Ⅱ', 'Ⅳ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅱ']

love_meet(bob, alice)

# Exercise 2
def affair_meet(bobPaths, alicePaths, silvesterPath):
    bobSet = set(bobPaths)
    aliceSet = set(alicePaths)
    silvesterSet = set(silvesterPath)
    print((aliceSet & silvesterSet) - bobSet)


alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

affair_meet(bob, alice, silvester)