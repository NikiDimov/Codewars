def dig_pow(n, p):
    sums = 0
    new_list = [int(el) for el in str(n)]
    for el in new_list:
        sums += el ** p
        p += 1
    if sums % n == 0:
        return sums // n
    return -1


print(dig_pow(89, 1))
