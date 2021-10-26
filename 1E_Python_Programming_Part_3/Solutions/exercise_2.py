#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:22:44 2020

@author: dan
"""

import random

class Patient:
    def __init__(self, name, patient_id, age):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.cured = False
        
    def attend_ed(self, mean_time):
        time_spent_in_ed = random.expovariate(1 / mean_time)
          
        print (f"{self.patient_id} : {self.name} was in ED for",
               f"{time_spent_in_ed:.1f} minutes")
        
    def receive_treatment(self, prob_cure):
        if random.uniform(0, 1) < prob_cure:
            self.cured = True
            
        if self.cured == True:
            print (f"{self.patient_id} : {self.name} was CURED, with a",
                   f"cure probability of {prob_cure*100:.1f}%")
        else:
            print (f"{self.patient_id} : {self.name} was not cured, with a",
                   f"cure probability of {prob_cure*100:.1f}%")
            
patient_1 = Patient("Bob Smith", 1253617, 61)
patient_2 = Patient("Mary Jones", 5439812, 55)

patient_1.attend_ed(60)
patient_1.receive_treatment(0.3)

patient_2.attend_ed(180)
patient_2.receive_treatment(0.8)

