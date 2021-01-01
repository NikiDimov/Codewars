def howmuch(m, n):
    list_of_results = []
    sorted_list = sorted([m, n])
    for f in range(sorted_list[0], sorted_list[1] + 1):
        c = (f - 1) // 9
        b = (f - 2) // 7
        if 1 + 9 * c == 2 + 7 * b == f:
            money = f"M: {f}"
            boat = f"B: {b}"
            car = f"C: {c}"
            result = [money, boat, car]
            list_of_results.append(result)
    return list_of_results


print(howmuch(1, 100))
