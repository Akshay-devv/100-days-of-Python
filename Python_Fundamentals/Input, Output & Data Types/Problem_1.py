# Q1. Shopping Bill

# Ask the user for:
# Item Name
# Price
# Quantity

# Print:
# Item Name
# Total Cost
# Data type of each input

item_name = input("Enter Item Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

total_cost = price * quantity

print("\n========== SHOPPING BILL ==========")
print("Item Name   :", item_name)
print("Price       :", price)
print("Quantity    :", quantity)
print("Total Cost  :", total_cost)

print("\n====== DATA TYPES ======")
print("Item Name :", type(item_name))
print("Price     :", type(price))
print("Quantity  :", type(quantity))