# Chapter Notes
#region
# Lists are collections of items (in order)
# Items do not need to be of the same data type
#
# Syntax: Surround a list with square brackets []
#         Separate items with commas
#         e.g.:     numbers = [1, 2, 3, 4, 5]
#                   number_names = ["one", "two", "three"]
#
# List indices are zero-based and allow backward-indexing, so:
#   First item is list_name[0]
#   Last item is list_name[-1]
#endregion

print("Chapter 3:")
print("Exercise 1 - Creating a List")

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[1].title())
print(bicycles[-2].upper())

message = f"My favorite bicycle was a {bicycles[0].title()}."
print(message)
