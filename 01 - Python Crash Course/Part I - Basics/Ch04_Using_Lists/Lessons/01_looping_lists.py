"""Chapter 4: Lesson 1"""

print("Chapter 4:")
print("Exercise 1 - Looping in lists")

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)

# A colon-indicated block can have multiple lines of code
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")
# Whitespace indenting matters.
# Since this is outdented one tab, this will only execute after the loop completes.
print("Thank you everyone. That was a great magic show!\n")
