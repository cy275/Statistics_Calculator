"""
    z represents z score, describes the standard deviation of those sample means (the standard error).
    x represents random sample
    μ represents mean
    σ represents standard deviation
    n represents number of sample
"""


def z_score(z, x, μ, σ, n):
    # below is Z score formula
    z = (x - μ) / (σ / n ** 0.5)
    return z
