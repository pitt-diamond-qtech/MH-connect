'''
This is attempting to be a 'one-click experiment', where the functions in this module connect to the MultiHarp,
begin a data stream, write to a data file, decode the data, and plot the data.

Currently it doesn't work because A) the data decoding appears incorrect and B) a sys.exit() call is interrupting
execution.
'''

import numpy as np
import matplotlib.pyplot as plt

from tttrmode import run_T3_to_txt

DATA_PATH = 'C:\\Users\\Boris\\Dropbox\\Documents\\Duttlab\\data\\'

def read_tttrmode_txt(filename):
    
    f = open(filename, "r")

    line = f.readline()
    times = np.fromstring(line, sep=', ', dtype=np.int)

    return times

def basic_plot(times):
    times = read_tttrmode_txt('t3_2.txt')
    x = np.arange(0,len(times))
    plt.scatter(x,times)
    plt.xlim([0,4000])
    plt.ylim([0,2e7])
    plt.show()

def clean_up_anomalies(times):
    
    timesClean = times[np.where(times != 2147483647)]
    
    timesClean = np.unique(timesClean)
    return timesClean
    
    
#%% 

data_filename='t3_5.txt'
run_T3_to_txt(data_filename)

#%%
data_filename='t3_4.txt'
times = read_tttrmode_txt(data_filename)
times = clean_up_anomalies(times)

plt.hist(np.diff(times),bins=1000)
plt.show()


data_filename='t3_5.txt'
times = read_tttrmode_txt(data_filename)
times = clean_up_anomalies(times)

plt.hist(np.diff(times),bins=1000)
