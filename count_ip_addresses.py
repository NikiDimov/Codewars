from ipaddress import ip_address


def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


print(ips_between("20.0.0.10", "20.0.1.0"))
