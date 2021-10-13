#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:52:35 2019

@author: dan
"""

import random

high_score = 0
continue_play = True

while continue_play == True:
    print ("Welcome to the game.  I'm thinking of a number between 1 and 100.")
    print ("Can you guess what number I'm thinking of?")
    print ()
    
    computer_number = random.randint(1,100)
    
    number_of_guesses = 10
    correctly_guessed = False
    score = 1000
    list_of_guesses = []
    
    for i in range(number_of_guesses):
        print (f"This is guess number {i+1}")
        user_guess = int(input("INPUT YOUR GUESS : "))
        
        list_of_guesses.append(user_guess)
            
        if user_guess == computer_number:
            print ("Correct!  Well done.")
            print (f"You scored {score}")
            print (f"Your guesses : {list_of_guesses}")
            correctly_guessed = True
            break
        elif user_guess < computer_number:
            print ("Too low.")
            score -= 100
        else:
            print ("Too high.")
            score -= 100
    
    if correctly_guessed == False:
        print ("You lose.")
        print (f"Your guesses : {list_of_guesses}")
        
    if score > high_score:
        print (f"NEW HIGH SCORE - {score}")
        high_score = score
        
    play_again_choice = input("Type Y to play again : ")
    
    if play_again_choice != "Y":
        continue_play = False
        
