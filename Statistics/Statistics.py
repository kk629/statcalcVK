from Calculator.Calculator import Calculator
from Statistics.PopulationMean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import st_dev
from Statistics.ConfidenceInterval import confidenceinterval
from Statistics.Zscore import zscore
from Statistics.PopulationVariance import pop_variance
from Statistics.SampleStandardDeviation import sampst_dev
from Statistics.SampleMean import samp_mean


#class Calculator:
    #result = 0

    #def __init__(self):
        #pass
class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def popmean(self, a):
        self.result = mean(a)
        return self.result

    def sammean(self, a):
        self.result = samp_mean(a)
        return self.result

    def med(self, a):
        self.result = median(a)
        return self.result

    def mod(self, a):
        self.result = mode(a)
        return self.result

    def stddev(self, a):
        self.result = st_dev(a)
        return self.result

    def sampstdev(self, a):
        self.result = sampst_dev(a)
        return self.result

    def confintv(self, a, b):
        self.result = confidenceinterval(a, b)
        return self.result

    def z_score(self, a):
        self.result = zscore(a)
        return self.result

    def pvariance(self, a):
        self.result = pop_variance(a)
        return self.result