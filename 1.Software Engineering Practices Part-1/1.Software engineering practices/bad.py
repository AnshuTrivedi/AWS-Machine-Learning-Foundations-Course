#!/usr/bin/env python
# coding: utf-8

# ### s is test scores list and i as educator trying to improve score of each students for better results



s=[88,92,79,93,85]
print(sum(s)/len(s))





s1=[]

for x in s:
    s1.append(x+5)

print(sum(s1)/len(s1))





s2=[]

for x in s:
    s2.append(x+10)
    
print(sum(s2)/len(s2))




s3=[]

for x in s:
    s3.append(x**0.5*10)
    
print(sum(s3)/len(s3))


# # This code looks repetitive and not clear what it is about,this is example of spaghetti code.
