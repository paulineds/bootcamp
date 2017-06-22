#in this file you can find usefull code such as the ECDF function
#to caal one of the function in this file use 'import bootcamp_utils_code as 'cdf'or other alias
#then call the function in the code with  alias.ecdf(data) (alias.functionin fileyouwanttouse(data))


import numpy as np


def ecdf(data):
    """ Compute the empiric cumulative distribution of the data"""

    x = np.sort(data)
    y = np.arange(1,len(data)+1)/float(len(data))
    return (x,y)
