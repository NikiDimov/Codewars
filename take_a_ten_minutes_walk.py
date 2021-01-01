def is_valid_walk(walk):

    count_n = 0
    count_s = 0
    count_e = 0
    count_w = 0

    if len(walk)==10:
        for el in walk:
            if el == "n":
                count_n += 1
            elif el == "s":
                count_s += 1
            elif el == "e":
                count_e += 1
            elif el == "w":
                count_w += 1
        if count_n == count_s and count_e == count_w:
            return True
        else:
            return False
    else:
        return False

