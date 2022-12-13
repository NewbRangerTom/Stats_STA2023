####################################################################
# Elementary Statistics STA2023: Chapter 8
#       confidence intervals
#       margin of error
#       sample size
#
#   Author: NewbRangerTom           Date: 02 November 2022

"""
class:
    conf_interval:
methods:
    dof:
        calculate the degree of freedom
            sample size
    standard_z_score:
        calculate z_score from chapter 6
            mean (provided or calculated)
            x (discrete radnom variable - interger or float, positive or negative)
            sigma (standard diviation)
    t_dist:
        getting the t-distribution for degree of freedom > 75
            confidence interval percent
    moe_known_sigma:
        calculating E (margin of error) and rounding to 4 decimal places
            sigma 
            z_score (provided or calculated)
    moe_unknown_sigma:
        calculating E from unknown sigma
            t_distribution
            sample standard diviation
            sample size
    find_sample_size:
        finding unknown sample size from:
            margin of error (E (margin of error from known sigma) or
                            moe (margin of error from unknown sigma) )
            sigma - standard diviation (sd),
            z-score (provided or from either t_dist or standard z_score methods)
    confidence_interval:
        finding the Confidence Interval of the given data
            alpha
            degree of freedom (sample size - 1)
            mean
            error (E or moe)
            two-tails (boolian true or false)
    tail_tscore:
        calculating the t-distribution
            degree of freedom (sample size - 1)
            confidence interval percent
            two-tails (boolian true or false)
"""
import numpy as np
from decimal import Decimal as dec
from math import sqrt
from scipy import stats

class conf_interval:
    def __init__(self) -> None:
        pass

    def dof(self, sample_size: int) -> int:                               
        self.sample_size = sample_size

        df = sample_size - 1
        return df

    def standard_z_score(self, mu: float, x: float, sigma: float) -> float:
        self.mean = mu
        self.x = x              # represents some number
        self.sigma = sigma
        
        z = (x - mu) / sigma
        return z

    def t_dist(self, confidence: float) -> float:                        
        # Confidence Interval Percents (z-scores / t-score where df > 75)
        z_scores = [(0.80,  1.2821),
                    (0.90,  1.6450),
                    (0.95,  1.9602),
                    (0.98,  2.3267),
                    (0.99,  2.5763),
                    (0.999, 3.2915)
                    ]
        i, z = 0, 0.0
        for score in z_scores:
            if score[i] == confidence:
                z = score[1]
        return z

    def moe_known_sigma(self, z: float, sigma: float, sample_size: int) -> float:                     
        E = round(dec(z * (sigma/sqrt(sample_size))), 4)          # (z_score * sigma/sqrt of sample_size)
        E = float(E)
        return E

    def moe_unknown_sigma(self, t: np.ndarray, s: float, sample_size: int) -> np.ndarray:
        self.t = t
        self.s = s
        self.sample_size = sample_size
        
        E = t * (s / sqrt(sample_size))
        return E

    def find_samp_size(self, z: float, moe: float, sigma: float) -> int:
        self.z = z
        self.moe = moe
        self.sigma = sigma
        
        num = ((z*sigma)/moe)**2
        num = int(num)
        return num

    def confidence_interval(self, alfa: float, df: int, mean: float, error: float, two_tails: bool) -> tuple:
        self.alfa = alfa
        self.df = df
        self.mean = mean
        self.error = error
        self.two_tails = two_tails
        
        if two_tails == False:
            ci = stats.t.interval(alpha = alfa, df = df, loc = mean, scale = error)
        else:
            ci = stats.t.interval(alpha = alfa/2, df = df, loc = mean, scale = error)
        return ci

    def tail_tscore(self, degree_of_freedom: int, confidence_interval_percent: float, two_tails: bool) -> np.ndarray:
        self.degree_of_freedom = degree_of_freedom
        self.confidence_interval_percent = confidence_interval_percent
        self.two_tails = two_tails
        
        if two_tails == False:
            # one-tailed test
            t_dist = stats.t.ppf(1 - (confidence_interval_percent / 2), degree_of_freedom)      
        else:
            # two-tailed test
            t_dist = stats.t.ppf(1 - confidence_interval_percent, degree_of_freedom)            
        return t_dist 

### END OF CLASS