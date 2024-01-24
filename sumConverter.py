# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:00:33 2024

@author: Max McMahon

solution to quiz prompt in Ardit Sulce's Python Mega Course on Udemy:
take in a list of strings (that are numbers) and convert into floats then return their total sum

"""

#my initial solution
def sumConverter(array):
    float_true = [float(i) for i in array]
    print(float_true)
    i = 0
    newSum = 0
    while i < len(float_true):
        newSum += float(float_true[i])
        i+=1
    return newSum
    
nums = ['1.2','7.2','4.5']
sumConverter(nums)

#################
#################

#my optimal solution
def sumConverter(array):
    newSum = 0
    newSum = sum(float(i) + newSum for i in array)
    return newSum

nums = ['1.2','7.2','4.5']
sumConverter(nums)
