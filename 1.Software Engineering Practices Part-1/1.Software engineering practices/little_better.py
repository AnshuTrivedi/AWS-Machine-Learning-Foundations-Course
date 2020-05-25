#!/usr/bin/env python
# coding: utf-8

import numpy as np 
import math



test_scores=[88,92,79,93,85]

print(np.mean(test_scores))



curved_5=[score + 5 for score in test_scores]

print(np.mean(curved_5))



curved_10=[score + 10 for score in test_scores]

print(np.mean(curved_10))



curved_sqrt=[math.sqrt(score)*10 for score in test_scores]

print(np.mean(curved_sqrt))


# # Used list comprehensions to make it more concise and readable,more descriptive names for resulting lists and variables,used numpy for mean calculation

# # Still curved_5 and curved_10 have same code logic ,we can generalise it into function. Code can be refactored.
