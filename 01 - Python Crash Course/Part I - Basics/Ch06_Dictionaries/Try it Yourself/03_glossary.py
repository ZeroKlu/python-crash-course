"""Assignment 6.3"""

# Glossary: A Python dictionary can be used to model an actual dictionary.
#           However, to avoid confusion, let's call it a glossary.
#           • Think of five programming words you’ve learned about in
#             the previous chapters. Use these words as the keys in your
#             glossary, and store their meanings as values.
#           • Print each word and its meaning as neatly formatted output.
#             You might print the word followed by a colon and then its
#             meaning, or print the word on one line and then print its
#             meaning indented on a second line. Use the newline character
#             (\n) to insert a blank line between each word-meaning pair
#             in your output.

print("Try-it-Yourself:")
print("Assignment 6.3")

coding_terms = {
    "Program": "A collection of instructions, which perform a specific task",
    "Boolean": "An expression used for statements that are TRUE or FALSE",
    "Bug": "A term used to denote an error or defect in hardware or software",
    "Object": "Combination of related variables, which can be used together.",
    "Code": "A set of instructions using the protocols of a given language",
}

print(f"\nProgram:\n{coding_terms['Program']}")
print(f"\nBoolean:\n{coding_terms['Boolean']}")
print(f"\nBug:\n{coding_terms['Bug']}")
print(f"\nObject:\n{coding_terms['Object']}")
print(f"\nCode:\n{coding_terms['Code']}")
