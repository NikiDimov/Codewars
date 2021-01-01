def unique_in_order(iterable):
    result = []
    if len(iterable) == 0:
        return result
    result.append(iterable[0])
    if len(iterable) > 1:
        for index in range(1, len(iterable)):
            if not iterable[index] == iterable[index - 1]:
                result.append(iterable[index])

    return result


unique_in_order('ABBCcAD')
