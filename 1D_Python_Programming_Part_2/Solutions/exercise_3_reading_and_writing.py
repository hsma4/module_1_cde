#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:46:45 2019

@author: dan
"""

# Import the csv library
import csv

list_of_names = []
list_of_vacc = []
list_of_ages = []
list_of_counties = []

# Read the file and put each data value in each row in the appropriate list
with open("input_data.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    
    for row in reader:
        list_of_names.append(row[0])
        list_of_vacc.append(row[1])
        list_of_ages.append(int(row[2]))
        list_of_counties.append(row[3])
        
# Take the length of the list of names to find how many records read in
number_of_patient_records = len(list_of_names)
print(f"{number_of_patient_records} records read in.")

# Calculate the mean age and round to 2 dp
average_age = sum(list_of_ages) / len(list_of_ages)
average_age = round(average_age, 2)
print(f"Average age of patients is {average_age}.")

number_in_Cornwall = 0
number_in_Devon = 0
number_in_Somerset = 0

# Count up the records for each county
for county in list_of_counties:
    if county == "Cornwall":
        number_in_Cornwall += 1
    elif county == "Devon":
        number_in_Devon += 1
    elif county == "Somerset":
        number_in_Somerset += 1
        
print(f"Patients living in Cornwall : {number_in_Cornwall}")
print(f"Patients living in Devon    : {number_in_Devon}")
print(f"Patients living in Somerset : {number_in_Somerset}")

number_vacc = 0
number_unvacc = 0

# Count the number of vaccinated and unvaccinated, and then calculate the % 
# split and round to 2 dp
for vacc_status in list_of_vacc:
    if vacc_status == "Yes":
        number_vacc += 1
    elif vacc_status == "No":
        number_unvacc += 1
        
percentage_vacc = (number_vacc / (number_vacc + number_unvacc)) * 100
percentage_vacc = round(percentage_vacc, 2)
percentage_unvacc = 100 - percentage_vacc
percentage_unvacc = round(percentage_unvacc, 2)

print(f"{percentage_vacc}% of patients are vaccinated")
print(f"{percentage_unvacc}% of patients are unvaccinated")

# Set up lists ready for writing to csv
list_of_column_names = ["Number of Records", 
                        "Mean Age", 
                        "No. in Cornwall",
                        "No. in Devon", 
                        "No. in Somerset", 
                        "% Vaccinated",
                        "% Unvaccinated"]
list_of_results = [number_of_patient_records,
                   average_age,
                   number_in_Cornwall,
                   number_in_Devon,
                   number_in_Somerset,
                   percentage_vacc,
                   percentage_unvacc]

list_of_lists_to_write = [list_of_column_names, list_of_results]

# Write results to csv file
with open("results.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    
    for sublist in list_of_lists_to_write:
        writer.writerow(sublist)

