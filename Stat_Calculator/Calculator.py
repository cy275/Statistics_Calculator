from Stat_Calculator.Z_Score import z_score


class Calculator:
    result = 0

    def __init__(self):
        pass

    def z(self, z, x, μ, σ, n):
        self.result = z_score(z, x, μ, σ, n)
        return self.result
