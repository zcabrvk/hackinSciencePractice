brace_map = {
    "(": ")",
    "<": ">",
    "[": "]",
    "{": "}"
}

def is_dyck_word(word: str) -> bool:
    diff = 0
    opening_brace = word[0]
    closing_brace = brace_map.get(opening_brace, False)

    if closing_brace is False:
        return False

    for count, i in enumerate(word):
        if i == opening_brace:
            diff = diff + 1
        elif i == closing_brace:
            diff = diff - 1
        else:
            return False

    return True if diff == 0 else False

# True
print(is_dyck_word("()"))
print(is_dyck_word("(((())))"))
print(is_dyck_word("()()()()"))
print(is_dyck_word("()(())()"))

# False
print("-----")
print(is_dyck_word("((("))
print(is_dyck_word(")"))
print(is_dyck_word("((()"))
print(is_dyck_word("()))"))

# True
print("-----")
print(is_dyck_word("[]"))
print(is_dyck_word("{}"))
print(is_dyck_word("<>"))
print(is_dyck_word("[[]]"))
print(is_dyck_word("{{}}"))
print(is_dyck_word("<<>>"))
print(is_dyck_word("[][]"))
print(is_dyck_word("{}{}"))
print(is_dyck_word("<><>"))