from Stat_Calculator.Standard_Deviation import standard_deviation
from Stat_Calculator.Population_Mean import mean


def z_score(a):
    z = (a - mean(a)) / len(a)
    return z
