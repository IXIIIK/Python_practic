from functools import reduce
from operator import truth, getitem

def keep_truthful(itr): 
    return filter(truth, itr)

def abs_sum(itr):
    return sum(map(abs, itr))

def walk(dct, itr): 
    return reduce(getitem, itr, dct)
