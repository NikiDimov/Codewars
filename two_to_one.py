def longest(s1, s2):
    new_string = s1 + s2
    list1 = []
    list1[:0] = new_string
    result = ''.join(sorted(set(list1)))
    return result


longest("inmanylanguages", "theresapairoffunctions")
