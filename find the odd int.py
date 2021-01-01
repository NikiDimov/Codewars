def find_it(seq):
    for el in seq:
        if seq.count(el) % 2 == 1:
            result = el
            return result
    return None


find_it([10])
