def productFib(prod):
    if prod == 0:
        return [0, 1, True]
    a = 0
    b = 1
    while True:
        n = (a + b)
        a = n - a
        b = n
        if a * b == prod:
            return [a, b, True]
        elif a * b > prod:
            return [a, b, False]


print(productFib(0))
