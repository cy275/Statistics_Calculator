"""
    σ2 represents population variance, is a measure of the spread of population data.
    x represents random sample
    μ represents mean
    n represents number of sample

"""


def population_variance(x, μ):
    # below is population variance formula
    σ2 = (x - μ) ** 2
    return σ2
