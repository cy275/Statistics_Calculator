"""
    z represents z score, tells you how many standard errors there are between the sample mean and the population mean.
    x represents random sample
    μ represents mean
    σ represents standard deviation
    n represents number of sample
"""


def z_score(z, x, μ, σ, n):
    # below is Z score formula
    z = (x - μ) / (σ / n ** 0.5)
    return z
