def xo(s):
    count_o = 0
    count_x = 0
    for char in s:
        if char.lower() == "o":
            count_o += 1
        elif char.lower() == "x":
            count_x += 1
    if count_x == count_o:
        return True
    return False


s = "zzoo"
print(xo(s))
