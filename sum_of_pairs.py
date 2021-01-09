def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
