import unicodedata

def is_anagram(word1, word2):
    def prepare_word(word):
        removed_spaces = word.replace(" ", "")
        removed_diacritics = unicodedata.normalize('NFD', removed_spaces).encode('ascii','ignore').decode('utf-8')
        lowercased = removed_diacritics.lower()
        return lowercased

    word1 = prepare_word(word1)
    word2 = prepare_word(word2)

    word1Count = dict()
    word2Count = dict()

    for i in word1:
        count = word1Count.get(i, 0)
        count = count+1
        word1Count[i] = count

    for i in word2:
        count = word2Count.get(i, 0)
        count = count+1
        word2Count[i] = count

    return word1Count == word2Count

print(is_anagram("crâné", "crane"))
print(is_anagram("Madam Curie", "Radium came"))
print(is_anagram("funeral", "real fun"))
