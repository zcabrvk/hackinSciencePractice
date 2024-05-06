def longest_word(text):
    cur = ""
    splitText = text.split()
    for i in splitText:
        if len(i) > len(cur):
            cur = i
    return cur

print(longest_word("We want a SHRUBBERY"))
print(longest_word("Shrubberies are great"))