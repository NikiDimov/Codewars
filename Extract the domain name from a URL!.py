import re


def domain_name(url):
    pattern = r"(https?://)?(www\d?\.)?(?P<domain>[\w-]+)\."
    result = re.finditer(pattern, url)
    for el in result:
        return el.group("domain")


print(domain_name("http://google.com"))
