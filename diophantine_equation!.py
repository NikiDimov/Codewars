from math import sqrt


def sol_equa(n):
    result = []
    x = n
    for x in range(n, 0, -1):
        y = (sqrt(abs(x ** 2 - n))) // 2
        if x ** 2 - 4 * y ** 2 == n:
            integers = [int(x), int(y)]
            result.append(integers)
    return result


sol_equa(90005)
