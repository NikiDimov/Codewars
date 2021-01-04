def duplicate_encode(word):
    word = [el.lower()for el in word]
    word = ''.join(word)
    result = ""
    for el in word:
        if el in word[word.find(el)+1:]:
            result += ")"
        else:
            result += "("
    return result


print(duplicate_encode("Success"))
