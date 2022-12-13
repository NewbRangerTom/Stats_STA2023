####################################################################
# Elementary Statistics STA2023: Chapter 4
#       discrete random variable
#
#   Author: NewbRangerTom           Date: 26 September 2022

"""
finding the mean of a discrete random variable set and the associated probabilities

class:
    mean_drv
methods:
    mean_drv
        calculates the mean of discrete random variables
            requires two lists (x and p(x) )
            checks list lengths to make sure number of variables match
            multiplies the variables in each list and appends to new list
            adds the variables in the new list together

EXAMPLE:

    from mybarplot import plot

    def main() -> None:
        x  = [   5,   11,   12,   13,   14,   16,   17]
        px = [0.13, 0.13, 0.34, 0.14, 0.11, 0.07, 0.08]
        title = 'Mean of Discrete Random Variable'
        xlabel = 'x'
        ylabel = 'p(x)'

        print(f'Mean = {mean_drv(x, px)}')                  # print the results
        plot(x, px, title, xlabel, ylabel)

    if __name__ == '__main__':
        main()

"""

class discrete_random_var:
    def __init__(self, a, b) -> None:
        self.a: list = a
        self.b: list = b

    def mean(self) -> float:
        xp = []
        if (len(self.a) != len(self.b)):
            raise ValueError("ERROR - lists are not same length")
        else:
            for vala, valb in zip(self.a, self.b):
                xp.append(vala * valb)
            mean = sum(xp)
        return mean