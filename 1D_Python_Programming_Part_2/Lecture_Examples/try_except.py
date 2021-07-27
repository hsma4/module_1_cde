#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:29:03 2021

@author: dan
"""

import random

def multiply_and_check(number_1, number_2):
    result = number_1 * number_2
    
    if result > 100:
        return True
    else:
        return False
    
try:
    user_input_1 = int(input("Enter number 1 : "))
except:
    print ("Sorry, you didn't input an integer")
    print ("We'll use a random integer instead")
    user_input_1 = random.randint(1,1000)
    print (f"Let's use {user_input_1}")
    
try:
    user_input_2 = int(input("Enter number 2 : "))
except:
    print ("Sorry, you didn't input an integer")
    print ("We'll use a random integer instead")
    user_input_2 = random.randint(1,1000)
    print (f"Let's use {user_input_2}")
    
is_result_over_100 = multiply_and_check(user_input_1, user_input_2)

if is_result_over_100 == True:
    print ("I knew you'd think of big numbers!")
    
