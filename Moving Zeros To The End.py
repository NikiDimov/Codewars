def move_zeros(array):
    counter = 0
    for el in array:
        if array[counter] == 0 and not isinstance(array[counter], bool):
            del array[counter]
            array.append(0)
        else:
            counter += 1
    return array


print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))
