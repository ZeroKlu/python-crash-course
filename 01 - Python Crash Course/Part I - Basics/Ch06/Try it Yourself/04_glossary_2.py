# Assignment 6.4
# Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3
#             by replacing your series of print() calls with a loop that runs through the dictionary’s
#             keys and values. When you’re sure that your loop works, add five more Python terms to your
#             glossary. When you run your program again, these new words and meanings should automatically
#             be included in the output.

print("Try-it-Yourself:")
print("Assignment 6.4")

coding_terms = {
    "Program": "An organized collection of instructions, which when executed perform a specific task or function",
    "Boolean": "An expression used for creating statements that are either TRUE or FALSE",
    "Bug": "A term used to denote an unexpected error or defect in hardware or software",
    "Object": "A combination of related variables, which can be selected and manipulated together.",
    "Code": "A written set of instructions, written using the protocols of a particular language",
}

for term, definition in coding_terms.items():
    print(f"\n{term}:\n{definition}")

print("-------------------------------------------------------------------")

more_coding_terms = {
    "List": "An ordered, mutable set of objects",
    "PEP 8": "The Python Enhancement Proposal is a style guide of Python code",
    "Literal": "A data item that has a fixed value",
    "Loop": "A loop is used for iterating over a sequence",
    "Module": "A module is a file consisting of Python code that can be imported and reused in a program",
}

coding_terms.update(more_coding_terms)
for term, definition in coding_terms.items():
    print(f"\n{term}:\n{definition}")
