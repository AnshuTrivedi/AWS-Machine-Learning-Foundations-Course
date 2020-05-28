#!/usr/bin/env python
# coding: utf-8


def nearest_square(num):
    """ Returns the nearest perfect square that is less than equal to num 
    Args:
    num: int. Input argument
    
    Return:
    root**2: int. Returns nearest perfect square that is less than equal to num
    """
    root=0
    while (root+1)**2<=num:
        root+=1
    return root**2
   

nearest_square(10)

