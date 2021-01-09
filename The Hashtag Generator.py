def generate_hashtag(s):
    if s == "":
        return False
    hashtag = "#"
    string = ""
    result = s.split()
    for el in result:
        string += el.capitalize()
    if len(string) > 140:
        return False
    return hashtag + string


print(generate_hashtag('codewars      '))
