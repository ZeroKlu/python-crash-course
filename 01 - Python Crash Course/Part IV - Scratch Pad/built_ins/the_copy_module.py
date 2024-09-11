# We previously used an open-ended slice [:] to make a copy of a list, but the copy module gives us another way

from copy import copy, deepcopy

# You can make a duplicate of a list (instead of a reference) using copy()
original_list = [1, 2, 3]
duplicate_list = copy(original_list)
# The lists are equivalent
print(original_list)
print(duplicate_list)
# But the IDs are different
print(f"{id(original_list)} | {id(duplicate_list)}")

# Using deepcopy() we can even do this for lists containing lists
orig_deep_list = [[1, 2, [3, 4, 5]], [6, 7], [8, 9]]
print(orig_deep_list)
dup_deep_list = deepcopy(orig_deep_list)
print(dup_deep_list)

# Note: In my testing, I got all of the dep copy using copy() as well, but we should use deepcopy as a convention
# dup_shallow_list = copy(orig_deep_list)
# print(dup_shallow_list)
