def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys


print(josephus([1, 2, 3, 4, 5, 6, 7], 3))
