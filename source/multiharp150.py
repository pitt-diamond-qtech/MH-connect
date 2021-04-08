'''
Basic class that abstracts the software connection to the physical MultiHarp 
150 device.

'''

import tttrmode


class MultiHarp150():
    def __init__(self):
        pass
    
    def establish_conn(self):
        pass
    
    def begin_t3_experiment(self, output_filename):
        
        tttrmode.run_T3_to_txt(self, output_filename)
        
    def begin_t2_experiment(self):
        pass

    # Acquisition time (in milliseconds)
    @property
    def tacq(self):
        return self.__tacq

    @tacq.setter
    def tacq(self, tacq):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    
    
        