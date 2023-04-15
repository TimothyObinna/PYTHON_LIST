# Task 3:
# Write a Python function that removes duplicates from an amount in a list and also sum up all the items and remove 7% VAT from that amount. And print the amount.

# ANSWER:
  
# List Items
Amount_list = [2000, 1200, 2000, 5000, 3000, 1200, 2500, 5000]

# Removal of Duplicates Values Using Set Function
Duplicate_Removal = set(Amount_list)

# Conversion Of Set To List
Set_to_List = list(Duplicate_Removal)

# Summation of the Total Values
Sum_list = sum(Set_to_List)

# VAT Calculation
Vat = 7/100 * Sum_list

# Removal of VAT From Summation List
Sum_list_Bal = Sum_list - Vat
print(Sum_list_Bal)