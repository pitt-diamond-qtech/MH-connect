'''
Basic class that abstracts the software connection to the physical MultiHarp 
150 device.

'''

import tttrmode


class MultiHarp150():
    def __init__():
        pass
    
    def establish_conn():
        pass
    
    def begin_t3_experiment(ofilename):
        
        tttrmode.run_T3_to_txt(ofilename)
        
    def begin_t2_experiment():
        pass
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    
    
        