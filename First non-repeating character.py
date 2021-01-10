def first_non_repeating_letter(string):
    new_list = list(string.lower())
    for i in range(len(new_list)):
        count = new_list.count(new_list[i])
        if count == 1:
            return string[i]
    return ''

print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))
