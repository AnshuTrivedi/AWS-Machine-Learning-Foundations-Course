#!/usr/bin/env python
# coding: utf-8


from nearest import nearest_square


print('Nearest square <=5 returned:{},actual answer is 4'.format(nearest_square(5)))
print('Nearest square <=-12 returned:{},actual answer is 0'.format(nearest_square(-12)))
print('Nearest square <=9 returned:{},actual answer is 9'.format(nearest_square(9)))
print('Nearest square <=23 returned:{},actual answer is 16'.format(nearest_square(23)))