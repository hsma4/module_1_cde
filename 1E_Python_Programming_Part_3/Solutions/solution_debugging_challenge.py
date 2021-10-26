#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:21:57 2020

@author: dan
"""

class Integer_Calculator:
    def __init__(self): # 1 - removed errant parameter switched_on
        self.switched_on = False
        
    def switch_on_calculator(self):
        self.switched_on = True # 2 - changed == to =
        print ("Calculator is now turned on") # 3 - added brackets; 4 - changed print message to reflect being turned on
        
    def switch_off_calculator(self):
        self.switched_on = False # 5 - changed == to =
        print ("Calculator is now turned off") # 6 - added brackets; 7 - changed print message to reflect being turned off
        
    def add_numbers(self, list_of_numbers):
        result = sum(list_of_numbers) # 8 - changed to correct variable name of list_of_numbers
        
        return result # 9 - return statement added
    
    def subtract_numbers(self, list_of_numbers): # 10 - added self to list of inputs
        result = list_of_numbers[0]
        
        for x in range(1, len(list_of_numbers)): # 11 - added missing bracket
            result -= list_of_numbers[x] # 12 - changed to correct operator of -=; 13 - changed list index to x
            
        return result
    
    def multiply_numbers(self, list_of_numbers):
        result = list_of_numbers[0] # 14 - added list index of [0]
        
        for x in range(1, len(list_of_numbers)):
            result = result * list_of_numbers[x] # 15 - changed to correct multiplication operator of *
            
        return result
    
    def divide_numbers(self, list_of_numbers): # 16 - added function inputs
        result = list_of_numbers[0]
        
        for x in range(1, len(list_of_numbers)):
            result = result / list_of_numbers[x]
            
        return result
    
    def input_numbers(self):
        if self.switched_on == False: # 17 - added self to refer to object instance's attribute; 18 - changed operator to == for comparison check
            print ("Calculator is switched off") # 19 - added indentation for if statement body; 20 - added brackets
            
            return []
        else:
            keep_inputting = True # 21 - changed default Boolean value to True to ensure while loop works
            list_of_inputs = [] # 22 - added creation of list_of_inputs so we can add to it below
            
            while keep_inputting == True: # 23 - changed to ==
                try:
                    input_number = int(input("Please input number : "))
                    list_of_inputs.append(input_number) # 24 - changed to correct function (append)
                    
                    valid_continue_decision = False # 25 - changed to False to make logic work
                    
                    while valid_continue_decision == False:
                        continue_decision = input("Continue (Y/N)? : ") # 26- removed integer casting (as we need to retain a string here)
                        
                        if continue_decision == "Y": # 27 - changed to ==
                            valid_continue_decision = True
                        elif continue_decision == "N": # 28 - changed to ==
                            valid_continue_decision = True
                            keep_inputting = False # 29 - added assignment of False to keep_inputting to make logic work
                            return list_of_inputs
                except: # 30 - changed to correct keyword of except
                    print ("You must input integers only") # 31 - added brackets
                    
    def input_operator(self):
        if self.switched_on == False:
            print ("Calculator is switched off")
            
            return "ERR" # 32 - changed to string "ERR", which is the correct format for returning from this function
        else: # 33 - changed to else (erroneously said except)
            valid_operator = False
            
            while valid_operator == False:
                print ("Please input : ")
                print ("+ for addition")
                print ("- for subtraction")
                print ("* for multiplication")
                print ("/ for division")
                selected_operator = input("SELECTION : ") # 34 - removed integer casting, as string required
                
                if selected_operator in ["+", "-", "*", "/"]: # 35 - changed operator from == to in
                    valid_operator = True
                    return selected_operator
                else: # 36 - changed to else (elif incorrect as no else if statement)
                    print ("Invalid operator")
                    
my_calculator = Integer_Calculator() # 37 - added storage of newly instatiated object as name my_calculator

my_calculator.switch_on_calculator() # 38 - corrected method name to switch_on_calculator; 39 - removed errant input value to method
list_of_input_numbers = my_calculator.input_numbers() # 40 - added variable to store output of input_numbers()
chosen_operator = my_calculator.input_operator() # 41 - added variable to store output of input_operator()

if len(list_of_input_numbers) > 1: # 42 - changed comparison to > 1 to make logic work; 43 - added : to if statement
    if chosen_operator == "+":
        answer = my_calculator.add_numbers(list_of_input_numbers) # 44 - added input to add_numbers()
    elif chosen_operator == "-": # 45 - changed to elif from elf
        answer = my_calculator.subtract_numbers(list_of_input_numbers) # 46 - added input to subtract_numbers()
    elif chosen_operator == "*": # 47 - changed to elif from elf
        answer = my_calculator.multiply_numbers(list_of_input_numbers) # 48 - added input to multiply_numbers()
    elif chosen_operator == "/": # 49 - changed to elif from elf
        answer = my_calculator.divide_numbers(list_of_input_numbers) # 50 - added input to divide_numbers
    else: # 51 - changed to else from els
        print ("Error - calculator was switched off")
    
    print (f"The answer is {answer}") # 52 - added brackets; 53 - added f before " to declare fString
else:
    print ("Only one number given")