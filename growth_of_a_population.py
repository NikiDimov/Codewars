def nb_year(p0, percent, aug, p):
    years = 0
    while not p0 >= p:
        p0 += p0 * percent * 0.01 + aug
        years += 1
    return years


nb_year(1500000, 0.25, 1000, 2000000)
