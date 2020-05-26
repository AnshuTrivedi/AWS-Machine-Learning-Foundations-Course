#!/usr/bin/env python
# coding: utf-8


import math
import numpy as np




def flat_curve(arr,n):
    return [i+n for i in arr]



def square_curve(arr,n):
    return [math.sqrt(i)*n for i in arr]



test_scores=[88,92,79,93,85]

curved_5=flat_curve(test_scores,5)

curved_10=flat_curve(test_scores,10)

curved_sqrt=square_curve(test_scores,10)



for score_list in test_scores,curved_5,curved_10,curved_sqrt:
    print(np.mean(score_list))

