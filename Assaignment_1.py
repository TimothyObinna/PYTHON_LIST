# Task 1:
# Write a Python program that sums up all the items in a list of 9 items; remove duplicates and print the result. 


# ANSWER:



mane = [1,1,2,4,5,6,4,5,6]

# Removal of Duplicate Values From List
duplicate_remove = set(mane)
# Conversion of Set To List
set_to_List = list(duplicate_remove)
# Using Sum Function for the Total Addition of the List Values
Sumed_list = sum(set_to_List)
print(Sumed_list)