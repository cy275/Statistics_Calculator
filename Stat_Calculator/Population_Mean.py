import statistics


def mean(a):
    # result = statistics.mean(a)

    for i in a:
        ttl = 0
        ttl = ttl + a[i]
    mu = ttl / len(a)
    return mu
