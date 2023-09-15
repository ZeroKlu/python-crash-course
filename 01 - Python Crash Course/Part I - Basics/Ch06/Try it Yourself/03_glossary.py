# Assignment 6.3
# Glossary: A Python dictionary can be used to model an actual dictionary.
#           However, to avoid confusion, let’s call it a glossary.
#           • Think of five programming words you’ve learned about in the previous chapters.
#             Use these words as the keys in your glossary, and store their meanings as values.
#           • Print each word and its meaning as neatly formatted output. You might print the word
#             followed by a colon and then its meaning, or print the word on one line and then print
#             its meaning indented on a second line. Use the newline character (\n) to insert a blank line
#             between each word-meaning pair in your output.

print("Try-it-Yourself:")
print("Assignment 6.3")

coding_terms = {
    "Program": "An organized collection of instructions, which when executed perform a specific task or function",
    "Boolean": "An expression used for creating statements that are either TRUE or FALSE",
    "Bug": "A term used to denote an unexpected error or defect in hardware or software",
    "Object": "A combination of related variables, which can be selected and manipulated together.",
    "Code": "A written set of instructions, written using the protocols of a particular language",
}

print(f"\nProgram:\n{coding_terms['Program']}")
print(f"\nBoolean:\n{coding_terms['Boolean']}")
print(f"\nBug:\n{coding_terms['Bug']}")
print(f"\nObject:\n{coding_terms['Object']}")
print(f"\nCode:\n{coding_terms['Code']}")
