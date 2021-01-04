def pig_it(text):
    result = []
    line = text.split()
    for el in line:
        if el[0].isalpha():
            result.append(el[1:] + el[0] + "ay")
        else:
            result.append(el)
    return ' '.join(result)


print(pig_it('O tempora o mores !'))
