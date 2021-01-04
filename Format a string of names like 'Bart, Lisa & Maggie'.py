def namelist(names):
    list1 = []
    index = 0
    for _ in names:
        list1.append(names[index]["name"])
        index += 1
    if len(list1) > 1:
        result = ", ".join(list1)
        k = result.rfind(", ")
        result = result[:k] + " &" + result[k + 1:]
        return result
    return ''.join(list1)


print(namelist([]))
