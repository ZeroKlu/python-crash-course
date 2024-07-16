print("Chapter 4:")
print("Exercise 1 - Looping in lists")

# If we look back at assignment 3.6, we spent a lot of time repeatedly printing the members of a list,
#   one at a time. That's really awful, and it violates the principle of not writing redundant code.
# Wouldn't it be neat if we had a way to look at all the items in a list and repeat an instruction on each one?
# Well, I have some good news for you!

magicians = ["alice", "david", "carolina"]
# In Python a "for" loop is like a "foreach" in C#
# Across Python, a line ending in a colon indicates the start of a block containing indented lines below it
for magician in magicians:
    print(magician)

# A colon-indicated block can have multiple lines of code
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")
# Whitespace indenting matters. Since this is outdented one tab, this will only execute after the loop completes.
print("Thank you everyone. That was a great magic show!\n")
