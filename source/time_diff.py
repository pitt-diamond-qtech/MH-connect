import numpy as np
import matplotlib.pyplot as plt
import Read_PTU

PATH = "..\\data\\"

def local_parser(stringy):

    tokens = []

    last_i = 0

    for i in range(0,len(stringy)):

        if stringy[i] == ' ':
            tokens.append(stringy[last_i:i])
            last_i = i

    tokens.append(stringy[last_i:len(stringy)])

    tokens_to_return = []

    for token in tokens:
        if token != ' ':
            tokens_to_return.append(token)

    return tokens_to_return


def timing_txt_to_list(shortfilename):

    '''
    Takes .cor files and returns the key information (throwing out metadata
    :param filename:
    :return: GAB (the correlation parameter)
    :return: tau (the timing delay)
    '''
    LEADING_LINES = 300
    TIME_COLUMN = 4

    filename = PATH + shortfilename

    time = []

    f = open(filename, "r")

    for i in range(0, LEADING_LINES):

        f.readline()

    print('\n\n')
    print('Parsing lines for ' + shortfilename)
    while (True):
        line = f.readline()
        line_data = local_parser(line)

        if line == '':
            break
        
        try:
            time.append(int(line_data[TIME_COLUMN]))
        except:
            pass

    print('Done!')
    return time

#%%
Read_PTU.read(PATH + 'regulartiming.ptu',PATH + 'regulartiming.txt')
Read_PTU.read(PATH + 'randomtiming.ptu',PATH + 'randomtiming.txt')



time = timing_txt_to_list('regulartiming.txt')

plt.hist(np.diff(time),bins=10)

time = timing_txt_to_list('randomtiming.txt')

plt.hist(np.diff(time),bins=10)
plt.show()
#print(time)
#byte = local_parser('8 CHN 0 808   806473       4092')
