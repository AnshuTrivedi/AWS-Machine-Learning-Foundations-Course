#!/usr/bin/env python
# coding: utf-8



from shirt import Shirt

shirt_one=Shirt('Red','M','long-sleeved',45)
shirt_two=Shirt('orange','S','short-sleeved',30)



print(shirt_one.color)
print(shirt_one.price)


shirt_two.change_price(45) # price change using method
print(shirt_two.price)


# How to access and change attribute values in python class

#  Shirt class has method to change shirt price
# Values can be changed either by assigning value or by  using method


shirt_one.color='Green'
print(shirt_one.color)


shirt_one.size='L'
print(shirt_one.size)


shirt_one.price=43
print(shirt_one.price)


# * There are some drawbacks to accessing attributes directly versus writing a method for accessing and displaying attributes.
# * Programming languages like C++/C  you can explicitely state wheather or not an object should be allowed to change or access attribute      values directly.
# * Changing value via method gives more flexibility in long term
