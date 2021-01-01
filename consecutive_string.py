def longest_consec(strarr, k):
    result = []
    if len(strarr) < k or len(strarr) == 0 or k <= 0:
        return ''
    for index in range(len(strarr)):
        result.append(''.join(strarr[index:index + k]))
    return max(result, key=len)


print(longest_consec([], 3))
