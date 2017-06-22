#in this file you can find usefull code such as the ECDF function
#to caal one of the function in this file use 'import bootcamp_utils_code as 'cdf'or other alias
#then call the function in the code with  alias.ecdf(data) (alias.functionin fileyouwanttouse(data))
#bootstrap function for stat analysis


import numpy as np


def ecdf(data):
    """ Compute the empiric cumulative distribution of the data"""

    x = np.sort(data)
    y = np.arange(1,len(data)+1)/float(len(data))
    return (x,y)


#bootstrap of the function chosen in argument (mean but can be standard dev...)
def bs_replicate(data, func=np.mean):
    """Compute a bootstrap replicate from data."""
    bs_sample = np.random.choice(data, size=len(data))

    return func(bs_sample)

def draw_bs_reps(data, func=np.mean, size=10000):
    """draw bootstrap replicate from 1d data"""
    return np.array([bs_replicate(data, func=func) for _ in range(size)])
