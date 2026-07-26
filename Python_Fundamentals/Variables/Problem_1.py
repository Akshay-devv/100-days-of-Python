# Challenge: Professional Salary Slip Generator

# Write a Python program to generate a professional salary slip for an employee.

# Requirements

# Store the following information in variables:

# Employee Name
# Employee ID
# Department
# Designation
# Basic Salary
# House Rent Allowance (HRA) – 20% of Basic Salary
# Dearness Allowance (DA) – 15% of Basic Salary
# Special Allowance
# Performance Bonus
# Provident Fund (PF) Deduction – 12% of Basic Salary
# Professional Tax (fixed amount)
# Income Tax – 10% of Gross Salary
# Tasks
# Calculate the Gross Salary.
# Calculate the Total Deductions.
# Calculate the Net Salary.
# Display the results in a neatly formatted salary slip.
# Constraints
# Use only variables, arithmetic operators, and print().
# Do not use:
# input()
# if / else
# Loops
# Functions
# String methods
# Lists, tuples, dictionaries, or any other data structures

# Your output should resemble a professional salary slip with clearly labeled sections for employee details, earnings, deductions, gross salary, total deductions, and net salary.


employee_name = "Akshay Balaji"
employee_id = "EMP1025"
department = "Data Engineering"
designation = "Data Engineer"

basic_salary = 50000
hra = basic_salary * 0.20
da = basic_salary * 0.15
special_allowance = 5000
performance_bonus = 8000


gross_salary = basic_salary + hra + da + special_allowance + performance_bonus


pf_deduction = basic_salary * 0.12
professional_tax = 200
income_tax = gross_salary * 0.10


total_deductions = pf_deduction + professional_tax + income_tax


net_salary = gross_salary - total_deductions

print("========================================")
print("            SALARY SLIP")
print("========================================")
print("Employee Name   :", employee_name)
print("Employee ID     :", employee_id)
print("Department      :", department)
print("Designation     :", designation)

print("\n----------- Earnings -----------")
print("Basic Salary        :", basic_salary)
print("HRA (20%)           :", hra)
print("DA (15%)            :", da)
print("Special Allowance   :", special_allowance)
print("Performance Bonus   :", performance_bonus)

print("--------------------------------")
print("Gross Salary        :", gross_salary)

print("\n---------- Deductions ----------")
print("PF (12%)            :", pf_deduction)
print("Professional Tax    :", professional_tax)
print("Income Tax (10%)    :", income_tax)

print("--------------------------------")
print("Total Deductions    :", total_deductions)

print("================================")
print("Net Salary          :", net_salary)
print("================================")