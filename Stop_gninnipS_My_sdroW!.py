def spin_words(sentence):
    text = sentence.split()
    result = ""
    for el in text:
        if len(el) >= 5:
            el = el[::-1]
        result += "".join(el) + " "
    return result.strip()


print(spin_words("Hello"))
