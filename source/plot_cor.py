"""
Some useful functions for plotting data obtained while using the multiharp 
GUI (which outputs .ptu and .phu filetypes).
"""

import matplotlib.pyplot as plt
import numpy as np

PATH = 'C:\\Users\\bmesi\\Dropbox\\Documents\\Duttlab\\MultiharpData\\'

def cor_to_list(filename):

    '''
    Takes .cor files and returns the key information (throwing out metadata)
    
      :param: filename
    
      :return: GAB (the correlation parameter)
      
      :return: tau (the timing delay)
    '''
    LEADING_LINES = 13
    TAU_COLUMN = 1
    GAB_COLUMN = 3

    filename = PATH + filename

    tau = []

    GAB = []

    f = open(filename, "r")

    for i in range(0, LEADING_LINES):

        line = f.readline()
        print(line)

    while (True):
        line = f.readline()
        line_data = np.fromstring(line, sep='\t')

        try:
            tau.append(line_data[TAU_COLUMN])
            GAB.append(line_data[GAB_COLUMN])
        except:
            break

    return tau, GAB


def plot_cor(filename):

    '''
    Creates a simple plot displaying the results of .cor files

        :param filename:
        
        :return: plot - handle to the figure
    '''

    tau, GAB = cor_to_list(filename)
    plt.figure()
    plt.plot(tau, GAB, linewidth=3)
    plt.xscale('log')
    plt.title(filename)
    plt.show()
