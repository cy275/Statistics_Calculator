from Stat_Calculator.Population_Mean import mean
from Stat_Calculator.Median import median
from Stat_Calculator.Mode import mode
from Stat_Calculator.Standard_Deviation import standard_deviation

from Stat_Calculator.Z_Score import z_score


class Calculator:
    result = 0

    def __init__(self):
        pass

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def mode(self,a):
        self.result = mode(a)
        return self.result

    def std_dev(self, a, b):
        self.result = standard_deviation(a, b)
        return self.result

    def z(self, z, x, μ, σ, n):
        self.result = z_score(z, x, μ, σ, n)
        return self.result
