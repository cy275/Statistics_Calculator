import statistics
from Stat_Calculator.Population_Mean import mean
from Stat_Calculator.Population_Variance import population_variance


def standard_deviation(a):
    # result = statistics.stdev(a, b)
    result = (population_variance(a)) ** 0.5
    return result
