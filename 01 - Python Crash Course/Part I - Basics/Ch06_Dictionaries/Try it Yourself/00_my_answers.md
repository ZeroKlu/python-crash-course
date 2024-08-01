## Chapter 6 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 6 try-it-yourself exercises.

---

### Assignment 6.1 - Person

Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as `first_name`, `last_name`, `age`, and `city`. Print each piece of information stored in your dictionary.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
person = { "first_name": "Scott", "last_name": "McLean", "age": 54, "city": "Lewisville" }
print(f"First Name: {person['first_name']}")
print(f"Last Name:  {person['last_name']}")
print(f"Age:        {person['age']}")
print(f"City:       {person['city']}")
```

</details>
<br>

Output:

```
First Name: Scott     
Last Name:  McLean    
Age:        54        
City:       Lewisville
```

---

### Assignment 6.2 - Favorite Numbers

Use a dictionary to store people's favorite numbers. Think of five names, and 
use them as keys in your dictionary. Think of a favorite number for each 
person, and store each as a value in your dictionary. Print each person's name 
and their favorite number. For even more fun, poll a few friends and get some 
actual data for your program.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
favorite_numbers = {
    "Scott": 42,
    "Andy": 37,
    "René": 343,
    "Matt": 12,
    "John": "√-1",
}

print(f"Scott's favorite number is {favorite_numbers['Scott']}")
print(f"Andy's favorite number is {favorite_numbers['Andy']}")
print(f"René's favorite number is {favorite_numbers['René']}")
print(f"Matt's favorite number is {favorite_numbers['Matt']}")
print(f"John's favorite number is {favorite_numbers['John']}")
```

</details>
<br>

Output:

```
Scott's favorite number is 42
Andy's favorite number is 37 
René's favorite number is 343
Matt's favorite number is 12
John's favorite number is √-1
```

---

### Assignment 6.3 - Glossary

A Python dictionary can be used to model an actual dictionary. However, to 
avoid confusion, let's call it a glossary.

* Think of five programming words you've learned about in the previous 
  chapters. Use these words as the keys in your glossary, and store their 
  meanings as values.
* Print each word and its meaning as neatly formatted output. You might print 
  the word followed by a colon and then its meaning, or print the word on one 
  line and then print its meaning indented on a second line. Use the newline 
  character `\n` to insert a blank line between each word-meaning pair in your 
  output.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
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
```

</details>
<br>

Output:

```
Program:
An organized collection of instructions, which when executed perform a specific task or function

Boolean:
An expression used for creating statements that are either TRUE or FALSE

Bug:
A term used to denote an unexpected error or defect in hardware or software

Object:
A combination of related variables, which can be selected and manipulated together.

Code:
A written set of instructions, written using the protocols of a particular language
```

---

### Assignment 6.4 - Glossary 2

Now that you know how to loop through a dictionary, clean up the code from 
Exercise 6.3 by replacing your series of print() calls with a loop that runs 
through the dictionary's keys and values. When you're sure that your loop 
works, add five more Python terms to your glossary. When you run your program 
again, these new words and meanings should automatically be included in the 
output.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
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
```

</details>
<br>

Output:

```
Program:
An organized collection of instructions, which when executed perform a specific task or function

Boolean:
An expression used for creating statements that are either TRUE or FALSE

Bug:
A term used to denote an unexpected error or defect in hardware or software

Object:
A combination of related variables, which can be selected and manipulated together.

Code:
A written set of instructions, written using the protocols of a particular language
-------------------------------------------------------------------

Program:
An organized collection of instructions, which when executed perform a specific task or function

Boolean:
An expression used for creating statements that are either TRUE or FALSE

Bug:
A term used to denote an unexpected error or defect in hardware or software

Object:
A combination of related variables, which can be selected and manipulated together.

Code:
A written set of instructions, written using the protocols of a particular language

List:
An ordered, mutable set of objects

PEP 8:
The Python Enhancement Proposal is a style guide of Python code

Literal:
A data item that has a fixed value

Loop:
A loop is used for iterating over a sequence

Module:
A module is a file consisting of Python code that can be imported and reused in a program
```

---

### Assignment 6.5 - Rivers

Make a dictionary containing three major rivers and the country each river runs through.

One key-value pair might be `nile`: `egypt`.

* Use a loop to print a sentence about each river, such as The Nile runs 
  through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
print()

for river in rivers.keys():
    print(river.title())
print()

for country in rivers.values():
    print(country.title())
```

</details>
<br>

Output:

```
The Nile runs through Egypt
The Amazon runs through Brazil
The Mississippi runs through United States

Nile
Amazon
Mississippi

Egypt
Brazil
United States
```

---

### Assignment 6.6 - Polling

Use the code in favorite_languages.py
* Make a list of people who should take the favorite languages poll. Include 
  some names that are already in the dictionary and some that are not.
* Loop through the list of people who should take the poll. If they have 
  already taken the poll, print a message thanking them for responding. If 
  they have not yet taken the poll, print a message inviting them to take the 
  poll.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people = ["jen", "sarah", "adam", "edward", "eleanor", "phil"]
for name in people:
    if name in favorite_languages.keys():
        print(f"Hi {name.title()}! Thanks for taking the poll.")
    else:
        print(f"Hi {name.title()}, please take the poll.")
```

</details>
<br>

Output:

```
Hi Jen! Thanks for taking the poll.
Hi Sarah! Thanks for taking the poll.
Hi Adam, please take the poll.
Hi Edward! Thanks for taking the poll.
Hi Eleanor, please take the poll.
Hi Phil! Thanks for taking the poll.
```

---

### Assignment 6.7 - People

Start with the program you wrote for Exercise 6.1. Make two new dictionaries 
representing different people, and store all three dictionaries in a list 
called people. Loop through your list of people. As you loop through the list, 
print everything you know about each person.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
person1 = { "first_name": "Scott", "last_name": "McLean", "age": 52, "city": "Lewisville" }
person2 = { "first_name": "Jeremy", "last_name": "McLean", "age": 47, "city": "Columbus" }
person3 = { "first_name": "Hillary", "last_name": "Taylor", "age": 50, "city": "Twinsburg" }
people = [person1, person2, person3]
for person in people:
    print()
    for key, value in person.items():
        print(f"{key} = {value}")
```

</details>
<br>

Output:

```
first_name = Scott
last_name = McLean
age = 52
city = Lewisville

first_name = Jeremy
last_name = McLean
age = 47
city = Columbus

first_name = Hillary
last_name = Taylor
age = 50
city = Twinsburg
```

---

### Assignment 6.8 - Pets

Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner's name. Store 
these dictionaries in a list called pets. Next, loop through your list and as 
you do, print everything you know about each pet.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
charlie = {
    "animal": "dog",
    "owner": "talia",
}

orville = {
    "animal": "guinea pig",
    "owner": "scott",
}

bronte = {
    "animal": "cat",
    "owner": "melissa",
}

pets = [charlie, orville, bronte]
for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}")
```

</details>
<br>

Output:

```
Talia owns a dog
Scott owns a guinea pig
Melissa owns a cat
```

---

