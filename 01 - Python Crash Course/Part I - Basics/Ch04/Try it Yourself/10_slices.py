# Assignment 4.10
# Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program
#         that do the following:
#         • Print the message The first three items in the list are:.
#           Then use a slice to print the first three items from that program’s list.
#         • Print the message Three items from the middle of the list are:.
#           Use a slice to print three items from the middle of the list. 
#         • Print the message The last three items in the list are:.
#           Use a slice to print the last three items in the list.

print("Try-it-Yourself:")
print("Assignment 4.10")

odd_numbers = list(range(1, 21, 2))
print(f"The first three odd numbers are: {odd_numbers[:3]}")
print(f"The next three odd numbers are: {odd_numbers[3:6]}")
print(f"The last three odd numbers are: {odd_numbers[-3:]}")
