def rot13(message):
    result = ""
    for el in message:
        if el.isalpha():
            if ord(el) in range(65, 78):
                result += chr(ord(el) + 13)
            elif ord(el) in range(78, 91):
                result += chr(ord(el) - 13)
            elif ord(el) in range(97, 110):
                result += chr(ord(el) + 13)
            elif ord(el) in range(110, 123):
                result += chr(ord(el) - 13)
        else:
            result += el

    return result


print(rot13("Test"))
