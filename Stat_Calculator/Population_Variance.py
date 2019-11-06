from Stat_Calculator.Population_Mean import mean


def population_variance(a):
    # below is population variance formula
    ttl = 0
    for i in a:
        ttl = (a[i] - mean(a)) ** 2
        return ttl
    result = ttl / len(a)
    return result
