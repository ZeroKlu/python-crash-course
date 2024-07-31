# Assignment 10.10
# Common Words: Visit Project Gutenberg (https:// gutenberg.org/) and find a few texts you'd like to analyze.
#               Download the text files for these works, or copy the raw text from your browser into a text file
#               on your computer. You can use the count() method to find out how many times a word or phrase
#               appears in a string. For example, the following code counts the number of times 'row' appears in a string:
#               ------------------------------------
#               >>> line = "Row, row, row your boat"
#               >>> line.count('row')
#               2
#               >>> line.lower().count('row')
#               3
#               ------------------------------------
#               Notice that converting the string to lowercase using lower() catches all appearances of the word
#               you're looking for, regardless of how it's formatted. Write a program that reads the files you
#               found at Project Gutenberg and determines how many times the word 'the' appears in each text.
#               This will be an approximation because it will also count words such as 'then' and 'there'.
#               Try counting 'the ', with a space in the string, and see how much lower your count is.

import os

ROOT_DIR = os.path.dirname(__file__)


def examine_file(file_name, search_words):
    """Count word occurrences in file passed"""
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    terminators = [" ", ".", ",", "?", "\n"]
    try:
        with open(file_path) as f:
            content = f.read().lower()
    except:
        print(f"\nFile {file_name} could not be found!")
    else:
        print(f"\nWord analysis in [{file_name}]:")
        for word in search_words:
            num = 0
            for start_term in terminators:
                for end_term in terminators:
                    num += content.count(f"{start_term}{word}{end_term}")
            print(f"{word}: {num}")


print("Try-it-Yourself:")
print("Assignment 10.10")

file_names = ["frankenstein.txt", "little_fuzzy.txt",
              "star_hunter.txt", "snow_crash.txt", "the_republic.txt"]
search_terms = ["man", "woman", "person"]

for file_name in file_names:
    examine_file(file_name, search_terms)
