# BMI Calculator

# Difficulty: Easy

# Problem

# Write a Python program that calculates a person's Body Mass Index (BMI).

# The program should:

# Read the user's weight in kilograms.
# Read the user's height in meters.
# Calculate the BMI using the formula:
# BMI=
# Height
# 2
# Weight
# 	​

# Display:
# Weight
# Height
# BMI
# Display the data type of:
# Weight
# Height
# BMI
# Input

# The program accepts two inputs:

# A floating-point number representing the weight (in kilograms).
# A floating-point number representing the height (in meters).
# Output

# Print:

# Weight
# Height
# Calculated BMI
# The data type of each of the three values
# Example 1
# Input
# 68
# 1.75
# Output
# Weight : 68.0 kg
# Height : 1.75 m
# BMI    : 22.20408163265306

# Weight Type : <class 'float'>
# Height Type : <class 'float'>
# BMI Type    : <class 'float'>
# Example 2
# Input
# 82.5
# 1.80
# Output
# Weight : 82.5 kg
# Height : 1.8 m
# BMI    : 25.462962962962962

# Weight Type : <class 'float'>
# Height Type : <class 'float'>
# BMI Type    : <class 'float'>
# Constraints
# Weight > 0
# Height > 0
# Convert user input to the appropriate numeric data type before performing calculations.
# Topics Covered
# Variables
# input()
# print()
# Data Types (float)
# Type Conversion
# Arithmetic Operators (/, **)
# type()


weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print("\n========== BMI REPORT ==========")
print("Weight :", weight, "kg")
print("Height :", height, "m")
print("BMI    :", bmi)

print("\n====== DATA TYPES ======")
print("Weight :", type(weight))
print("Height :", type(height))
print("BMI    :", type(bmi))