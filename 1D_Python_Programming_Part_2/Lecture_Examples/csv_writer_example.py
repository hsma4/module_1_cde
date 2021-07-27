#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:31:21 2021

@author: dan
"""


# Writing csv files is easy with the csv library too!

import csv

# Let's say we have some lists we want to write to file
list_of_trainers = ["Dan", "Kerry", "Sean", "Tom"]
list_of_numbers = [1,2,3,4]
list_of_lists = [list_of_trainers, list_of_numbers]

with open("output.csv", "w") as f:
    # Create a csv writer object that writes a csv file with comma delimiters
    writer = csv.writer(f, delimiter=",")
    
    # Write a row for each of our lists
    for sublist in list_of_lists:
        writer.writerow(sublist)
        
