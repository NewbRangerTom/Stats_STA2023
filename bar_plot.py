####################################################################
# Elementary Statistics STA2023:
#       basic bar graph for ploting data
#       this method was done simply to be done
#       this can be implemeneted directly in main
#
#   Author: NewbRangerTom           Date: 09 November 2022

"""
simple bar plot graphing function using matplotlib.pyplot

    title = graph title, accepts string
    xlab = x axis label, accepts string
    ylab = y axis label, accepts string
    lab_rot = label rotation, accepts interger from 0 to 90

"""

import matplotlib.pyplot as plt

def plot(a: list, b: list, title: str = 'bar graph', xlab: str = 'x', ylab: str = 'y', lab_rot: int = 45) -> None:
    if  lab_rot < 0 or lab_rot > 90:
        print(f'rotation must be between 0 and 90')
    else:
        # plot and show the graph
        fig, ax = plt.subplots()        # create graph objects
        fig.set_facecolor('orange')     # optional - set graph figure color
        ax.set_title(title)
        ax.set_xlabel(xlab)             # label x axis
        ax.set_ylabel(ylab)             # label y axis
        bar = ax.bar(a, b)              # set graph type and data
        ax.bar_label(bar, label_type = 'center', rotation = lab_rot)
        plt.show()                      # show graph