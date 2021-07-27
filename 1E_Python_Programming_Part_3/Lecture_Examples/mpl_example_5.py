#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:25:28 2020

@author: dan
"""

import matplotlib.pyplot as plt # provides matlab-style plotting interface

# Data to plot
hsma_trainers = ["Dan", "Kerry", "Sean", "Tom", "Luca"]
hours_of_teaching = [93, 6, 21, 9, 3]

figure_1, ax = plt.subplots()

ax.set_xlabel("Trainer")
ax.set_ylabel("Hours of Teaching on HSMA")

ax.bar(hsma_trainers, hours_of_teaching)

figure_1.show()

