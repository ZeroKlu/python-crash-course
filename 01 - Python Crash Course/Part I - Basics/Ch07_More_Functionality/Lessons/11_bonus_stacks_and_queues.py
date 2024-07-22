print("Chapter 7:")
print("Exercise 11 - Stacks and Queues")

# When processing items from an ordered collection like a list, we need to think about which end gets processed first.
#
# Using while loops, we can simulate the behavior of two different list-like data structures,
#   stacks and queues.

# A stack uses last-in, first-out (LIFO) order.
# You can imagine this visually. If you stack several things on top of each other, at any time
#   you can only remove the top one (the last one you added)
my_stack = [1, 2, 3, 4, 5]
print(f"Stack: {my_stack}")
while my_stack:
    # By default, pop() removes the last item from the list, but I will redundantly specify index -1
    print(my_stack.pop(-1))

# A queue uses first-in, first-out (FIFO) order
# This is a lot like when people are waiting in line
my_queue = [1, 2, 3, 4, 5]
print(f"\nQueue: {my_queue}")
while my_queue:
    # By popping the first item (index 0) each iteration, we maintain the queue order
    print(my_queue.pop(0))

# This isn't a complete illustration of stacks and queues, just of removal order
