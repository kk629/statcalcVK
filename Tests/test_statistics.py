import unittest
from Statistics.Statistics import Statistics
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        # test_data = CsvReader('/Tests/Data/meantest.csv').data
        # for row in test_data:
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.statistics.popmean(data), 3)
        # self.assertEqual(self.calculator.popmean(row['Value 1']), 16.5)
        # self.assertEqual(self.calculator.popmean(x), int(16.5))

    def test_sample_mean_calculator(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(self.statistics.sammean(data), 3)

    def test_median_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.statistics.med(data), 3.5)

    def test_mode_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1, 2, 3, 4, 5, 6, 3]
        self.assertEqual(self.statistics.mod(data), 3)

    def test_standard_deviation_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.statistics.stddev(data), 1.5811388300841898)

    # def test_sample_standard_deviation_calculator(self):
    #    data = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #    self.assertEqual(self.statistics.sampstdev(data), 1.5811388300841898)

    def test_confidence_interval_calculator(self):
        data = [1, 2, 3, 4, 5]
        conf = 95
        self.assertEqual(self.statistics.confintv(data, conf), (4.39, 1.61))

    def test_zscore_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.statistics.z_score(data), -1.2649110640673518)

    def test_population_variance_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.statistics.pvariance(data), 2.5000000000000004)


if __name__ == '__main__':
    unittest.main()