# Banking Profile

# Difficulty: Easy

# Problem

# Write a Python program that generates a Bank Account Summary for a customer.

# The program should:

# Read the following inputs from the user:
# Account Holder Name
# Account Number
# Current Balance
# Annual Interest Rate (in percentage)
# Calculate the Annual Interest using the formula:
# Annual Interest=
# 100
# Current Balance×Interest Rate
# 	​

# Display:
# Account Holder Name
# Account Number
# Current Balance
# Interest Rate
# Annual Interest
# Display the data type of every input.
# Input

# The program accepts four inputs:

# A string representing the account holder's name.
# A string representing the account number.
# A floating-point number representing the current account balance.
# A floating-point number representing the annual interest rate.
# Output

# Print:

# Account Holder Name
# Account Number
# Current Balance
# Annual Interest Rate
# Annual Interest
# The data type of each input
# Example 1
# Input
# Akshay Balaji
# 1234567890
# 50000
# 6.5
# Output
# ========== BANK ACCOUNT SUMMARY ==========
# Account Holder : Akshay Balaji
# Account Number : 1234567890
# Balance        : 50000.0
# Interest Rate  : 6.5%
# Annual Interest: 3250.0

# ========== DATA TYPES ==========
# Account Holder : <class 'str'>
# Account Number : <class 'str'>
# Balance        : <class 'float'>
# Interest Rate  : <class 'float'>
# Example 2
# Input
# John Doe
# 9876543210
# 125000
# 7.25
# Output
# ========== BANK ACCOUNT SUMMARY ==========
# Account Holder : John Doe
# Account Number : 9876543210
# Balance        : 125000.0
# Interest Rate  : 7.25%
# Annual Interest: 9062.5

# ========== DATA TYPES ==========
# Account Holder : <class 'str'>
# Account Number : <class 'str'>
# Balance        : <class 'float'>
# Interest Rate  : <class 'float'>
# Constraints
# Current Balance ≥ 0
# Interest Rate ≥ 0
# Convert numeric inputs to the appropriate data type before performing calculations.

account_holder = input("Enter Account Holder Name: ")
account_number = input("Enter Account Number: ")
current_balance = float(input("Enter Current Balance: "))
interest_rate = float(input("Enter Annual Interest Rate (%): "))

annual_interest = (current_balance * interest_rate) / 100

print("\n========== BANK ACCOUNT SUMMARY ==========")
print("Account Holder :", account_holder)
print("Account Number :", account_number)
print("Balance        :", current_balance)
print("Interest Rate  :", interest_rate, "%")
print("Annual Interest:", annual_interest)

print("\n========== DATA TYPES ==========")
print("Account Holder :", type(account_holder))
print("Account Number :", type(account_number))
print("Balance        :", type(current_balance))
print("Interest Rate  :", type(interest_rate))