import re


def solution(s):
    result = []
    pattern = r"[a-z]{2}"
    match = re.finditer(pattern, s)
    for el in match:
        result.append(el.group())
    if not len(s) % 2 == 0:
        result.append(s[-1] + "_")
    return result


s = "asdfadsf"

solution(s)
