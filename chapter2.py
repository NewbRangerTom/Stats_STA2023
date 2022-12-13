####################################################################
# Elementary Statistics STA2023: Chapter 2
#       quartiles
#       percentiles
#       grouped and ungrouped data
#           mean
#           variance
#           standard diviation
#
#   Author: NewbRangerTom           Date: 06 December 2022

"""
Quartiles
Variance and Standard Diviation for grouped and ungrouped data

class:  quartles
    methods:
        quarters: calclates the quartiles of a user provided list of intergers or floats
            data -> list of intergers or floats
            method -> Literal: 'inclusive' or 'exclusive'
        iqr: calculates the interquartile range
            dependant on quarters (q3 and q1 or quarters[2] and quarters[0])
            to calculate the difference between q3 and q1
        kth_percentile: calculates the value of the ith postion of a ranked data set
            kpercent -> interger representing the percent position of the data set
            data -> list of intergers or floats
        percentile_rank: calculates the rank of a given value within the range of a data set
            data -> list of intergers or floats
            a -> the value to be ranked
        data_range: calculates the range of values in a data set
            data -> list of intergers or floats

class:  grouped_data
    methods:
        mean: calculates the mean for a grouped data set
            midpoints -> list of midpoints
            freqs -> list of frequancies for each midpoint
            sample_size -> interger for number of samples
        variance: calculates the variance of a population or sample data set
            boolian: set to determine population or sample
            midpoints
            frequencies
            sample_size
        standard_div: calculates the standard diviation for a population or sample data set
            boolian
            midpoints
            frequencies
            sample_size

class:  ungrouped_data
    methods:
        mean: calculates the mean for a set of ungrouped data
            data -> list of intergers or floats
        variance: calculates the variance for a population or sample data set
            boolian: set to determine population or sample
            data
        standard_div: calculates the standard diviation for a population or sample data set
            boolian
            data

"""

from math import ceil, floor, sqrt
from statistics import quantiles

class quartles:
    def __init__(self, data) -> None:
        self.data: list = data

    def quarters(self, n: int, m) -> list:
        quarters = quantiles(data = self.data, n = n, method = m)
        return quarters

    def iqr(self, q3, q1) -> float:
        iqr = q3 - q1
        return iqr

    def kth_percentile(self, kpercent: int) -> float:
        n = len(self.data)
        ith_position = kpercent / 100*(n+1)
        if ith_position % 2 == 0:
            kth = self.data[int(ith_position) - 1]
            return kth
        else:
            kth = (self.data[floor(ith_position) - 1] + self.data[ceil(ith_position) + 1]) / 2
            return kth

    def percentile_rank(self, a: float) -> float:
        less_than_a = [i for i in self.data if i < a]
        x = len(less_than_a)
        y = self.data.count(a)
        rank = ((x + 0.5*y) / len(self.data))*100
        return rank

    def data_range(self) -> float:
        data = sorted(self.data)
        dr = max(data) - min(data)
        return dr


class grouped_data:
    def __init__(self, midpoints, freqs, sample_size) -> None:
        self.midpoints: list = midpoints
        self.freqs: list = freqs
        self.sample_size: int = sample_size

    def mean(self) -> float:
        res_list = [self.midpoints[i] * self.freqs[i] for i in range(len(self.midpoints))]
        mean = sum(res_list) / self.sample_size
        return mean

    def variance(self, p: bool) -> float:
        m_two_f = [self.midpoints[i]**2 * self.freqs[i] for i in range(len(self.midpoints))]
        mf = [self.midpoints[i] * self.freqs[i] for i in range(len(self.midpoints))]
        if p:
            sigma_sqrd = (sum(m_two_f) - (sum(mf)**2 / self.sample_size)) / self.sample_size
        else:
            sigma_sqrd = (sum(m_two_f) - (sum(mf)**2 / self.sample_size)) / self.sample_size-1
        return sigma_sqrd

    def standard_div(self, p: bool) -> float:
        m_two_f = [self.midpoints[i]**2 * self.freqs[i] for i in range(len(self.midpoints))]
        mf = [self.midpoints[i] * self.freqs[i] for i in range(len(self.midpoints))]
        if p:
            sd_sqrd = (sum(m_two_f) - (sum(mf)**2 / self.sample_size)) /self.sample_size
        else:
            sd_sqrd = (sum(m_two_f) - (sum(mf)**2 / self.sample_size)) / self.sample_size-1
        s_igma = sqrt(sd_sqrd)
        return s_igma


class ungrouped_data:
    def __init__(self, data) -> None:
        self.data: list = data

    def __repr__(self) -> str:
        return f'Data = {self.data}'

    def __str__(self) -> str:
        return f'{self.data}'

    def mean(self) -> float:
        mean = sum(self.data) / len(self.data)
        return mean

    def variance(self, p: bool) -> float:
        xsqrd = [i**2 for i in self.data]
        if p:
            sigma_sqrd = (sum(xsqrd) - (sum(self.data)**2 / len(self.data))) / len(self.data)
        else:
            sigma_sqrd = (sum(xsqrd) - (sum(self.data)**2 / len(self.data))) / len(self.data)-1
        return sigma_sqrd

    def standard_div(self, p: bool) -> float:
        xsqrd = [i**2 for i in self.data]
        if p:
            sigma_sqrd = (sum(xsqrd) - (sum(self.data)**2 / len(self.data))) / len(self.data)
        else:
            sigma_sqrd = (sum(xsqrd) - (sum(self.data)**2 / len(self.data))) / len(self.data)-1
        s_igma = sqrt(sigma_sqrd)
        return s_igma

### END OF CLASS