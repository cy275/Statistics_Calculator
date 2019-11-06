from Stat_Calculator.Population_Mean import mean
from Stat_Calculator.Standard_Deviation import standard_deviation


# pcc stands for Population Correlation Coefficient
def pcc(x, y):
    for i in x & y:
        result = ((x[i] - mean(x)) / standard_deviation(x)) * ((x[i] - mean(y)) / standard_deviation(y))
        value = 1/x * result
        return value
