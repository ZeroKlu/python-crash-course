## Chapter 5 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 5 try-it-yourself exercises.

---

### Assignment 5.1 - Conditional Tests

Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.

Your code should look something like this:

```python
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
#
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
```

* Look closely at your results, and make sure you understand why each line 
  evaluates to `True` or `False`.
* Create at least ten tests. Have at least five tests evaluate to True and 
  another five tests evaluate to False.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
make = "Dodge"
model = "Challenger"
print("Is make == 'fiat'? I predict False.")
print(make == "fiat")
print("Is make == 'dodge'? I predict False.")
print(make == "dodge")
print("Is make == 'Dodge'? I predict True.")
print(make == "Dodge")
print("Is case-insensitive make == 'dodge'? I predict True.")
print(make.lower() == "dodge")

print("Is model == 'charger'? I predict False.")
print(model == "charger")
print("Is model != 'charger'? I predict True.")
print(model != "charger")
print("Is model == 'challenger'? I predict False.")
print(model == "challenger")
print("Is model == 'Challenger'? I predict True.")
print(model == "Challenger")
print("Is case-insensitive model == 'charger'? I predict False.")
print(model.lower() == "charger")
print("Is case-insensitive model == 'challenger'? I predict True.")
print(model.lower() == "challenger") 
```

</details>
<br>

<details>
<summary>Output</summary>

```
Is make == 'fiat'? I predict False.
False
Is make == 'dodge'? I predict False.
False
Is make == 'Dodge'? I predict True.
True
Is case-insensitive make == 'dodge'? I predict True.
True
Is model == 'charger'? I predict False.
False
Is model != 'charger'? I predict True.
True
Is model == 'challenger'? I predict False.
False
Is model == 'Challenger'? I predict True.
True
Is case-insensitive model == 'charger'? I predict False.
False
Is case-insensitive model == 'challenger'? I predict True.
True
```

</details>

---

### Assignment 5.2 - More Conditional Tests

You don't have to limit the number of tests you create to ten. If you want to 
try more comparisons, write more tests and add them to conditional_tests.py.
Have at least one True and one False result for each of the following:

* Tests for equality and inequality with strings
* Tests using the lower() method
* Numerical tests involving equality and inequality, greater than and less 
  than, greater than or equal to, and less than or equal to
* Tests using the and keyword and the or keyword
* Test whether an item is in a list
* Test whether an item is not in a list

Solution:

<details>
<summary>Spoiler Code</summary>

```python
make = "Dodge"
model = "Challenger"
year = 2014

print("Is make == 'fiat'? I predict False.")
print(make == "fiat")
print("Is make != 'fiat'? I predict True.")
print(make != "fiat")

print("Is case-insensitive make == 'fiat'? I predict False.")
print(make.lower() == "fiat")
print("Is case-insensitive make == 'dodge'? I predict True.")
print(make.lower() == "dodge")

print("\nIs year == 2014? I predict True.")
print(year == 2014)
print("Is year == 2020? I predict False.")
print(year == 2020)
print("Is year != 2020? I predict True.")
print(year != 2020)
print("Is year > 2020? I predict False.")
print(year > 2020)
print("Is year >= 2020? I predict False.")
print(year >= 2020)
print("Is year < 2020? I predict True.")
print(year < 2020)
print("Is year <= 2020? I predict True.")
print(year <= 2020)

print("\nIs case-insensitive make == 'dodge' and model == 'charger'? I predict False.")
print(make.lower() == "dodge" and model.lower() == "charger")
print("Is case-insensitive make == 'dodge' and model == 'challenger'? I predict True.")
print(make.lower() == "dodge" and model.lower() == "challenger")
print("Is case-insensitive make == 'dodge' or model == 'charger'? I predict True.")
print(make.lower() == "dodge" or model.lower() == "charger")
print("Is case-insensitive make == 'dodge' or model == 'challenger'? I predict True.")
print(make.lower() == "dodge" or model.lower() == "challenger")
print("Is case-insensitive make == 'fiat' or model == 'spider'? I predict False.")
print(make.lower() == "fiat" or model.lower() == "spider")

stats = [2014, "dodge", "challenger"]
print("\nDoes stats contain 'fiat'? I predict False.")
print("fiat" in stats)
print("\nDoes stats contain 'dodge'? I predict True.")
print("dodge" in stats)
print("\nDoes stats not contain 'charger'? I predict True.")
print("charger" in stats)
print("\nDoes stats not contain 'challenger'? I predict False.")
print("challenger" in stats)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Is make == 'fiat'? I predict False.
False
Is make != 'fiat'? I predict True.
True
Is case-insensitive make == 'fiat'? I predict False.
False
Is case-insensitive make == 'dodge'? I predict True.
True

Is year == 2014? I predict True.
True
Is year == 2020? I predict False.
False
Is year != 2020? I predict True.
True
Is year > 2020? I predict False.
False
Is year >= 2020? I predict False.
False
Is year < 2020? I predict True.
True
Is year <= 2020? I predict True.
True

Is case-insensitive make == 'dodge' and model == 'charger'? I predict False.
False
Is case-insensitive make == 'dodge' and model == 'challenger'? I predict True.
True
Is case-insensitive make == 'dodge' or model == 'charger'? I predict True.
True
Is case-insensitive make == 'dodge' or model == 'challenger'? I predict True.
True
Is case-insensitive make == 'fiat' or model == 'spider'? I predict False.
False

Does stats contain 'fiat'? I predict False.
False

Does stats contain 'dodge'? I predict True.
True

Does stats not contain 'charger'? I predict True.
False

Does stats not contain 'challenger'? I predict False.
True
```

</details>

---

### Assignment 5.3- Alien Colors #1

Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of `green`, `yellow`, or `red`.
* Write an if statement to test whether the alien's color is green. If it is,
  print a message that the player just earned 5 points.
* Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

Solution:

<details>
<summary>Spoiler Code</summary>

```python
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points!")
alien_color = "green"
if alien_color == "green":
    print("You earned 10 points!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
You earned 10 points!
```

</details>

---

### Assignment 5.4 - Alien Colors #2

Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

* If the alien's color is green, print a statement that the player just earned 
  5 points for shooting the alien.
* If the alien's color isn't green, print a statement that the player just 
  earned 10 points.
* Write one version of this program that runs the if block and another that 
  runs the else block.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
You earned 10 points!
You earned 5 points!
```

</details>

---

### Assignment 5.5 - Alien Colors #3

Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

* If the alien is green, print a message that the player earned 5 points.
* If the alien is yellow, print a message that the player earned 10 points.
* If the alien is red, print a message that the player earned 15 points.
* Write three versions of this program, making sure each message is printed for 
  the appropriate color alien.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
alien_colors = ["green", "yellow", "red"]
for alien_color in alien_colors:
    if alien_color == "green":
        points = 5
    elif alien_color == "yellow":
        points = 10
    elif alien_color == "red":
        points = 15
    else:
        points = 0
    print(f"You earned {points} points!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
You earned 5 points!
You earned 10 points!
You earned 15 points!
```

</details>

---

### Assignment 5.6 - Stages of Life

Write an if-elif-else chain that determines a person's stage of life.

Set a value for the variable age, and then:

* If the person is less than 2 years old, print a message that the person is a 
  baby.
* If the person is at least 2 years old but less than 4, print a message that 
  the person is a toddler.
* If the person is at least 4 years old but less than 13, print a message that 
  the person is a kid.
* If the person is at least 13 years old but less than 20, print a message that 
  the person is a teenager.
* If the person is at least 20 years old but less than 65, print a message that 
  the person is an adult.
* If the person is age 65 or older, print a message that the person is an elder.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
age = int(input("Enter your age: "))
if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are a adult!")
else:
    print("You are an elder!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Enter your age: 54
You are a adult!
```

</details>

---

### Assignment 5.7 - Favorite Fruit

Make a list of your favorite fruits, and then write a series of independent if 
statements that check for certain fruits in your list.

* Make a list of your three favorite fruits and call it
* Write five if statements. Each should check whether a certain kind of fruit 
  is in your list. If the fruit is in your list, the if block should print a 
  statement, such as You like bananas!

Solution:

<details>
<summary>Spoiler Code</summary>

```python
favorite_fruits = ["grapefruit", "key lime", "apple", "blackberry"]
fruit = "peach"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "apple"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "guava"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "blackberry"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "grapefruit"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
```

</details>
<br>

<details>
<summary>Output</summary>
Output:

```
apple is one of your favorites
blackberry is one of your favorites
grapefruit is one of your favorites
```

</details>

---

### Assignment 5.8 - Hello Admin

Make a list of five or more usernames, including the name `admin`. 

Imagine you are writing code that will print a greeting to each user after they 
log in to a website. Loop through the list, and print a greeting to each user:
* If the username is `admin`, print a special greeting, such as:  
  `Hello admin, would you like to see a status report?`
* Otherwise, print a generic greeting, such as:  
  `Hello Jaden, thank you for logging in again.`


Solution:

<details>
<summary>Spoiler Code</summary>

```python
usernames = ["anna", "bob", "charlie", "diana", "admin"]
for user in usernames:
    if (user.lower() == "admin"):
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hello Anna, thank you for logging in again.
Hello Bob, thank you for logging in again.
Hello Charlie, thank you for logging in again.
Hello Diana, thank you for logging in again.
Hello admin, would you like to see a status report?
```

</details>

---

### Assignment 5.9 - No Users

Add an if test to hello_admin.py to make sure the list of users is not empty.
* If the list is empty, print the message We need to find some users!
* Remove all of the usernames from your list, and make sure the correct message 
  is printed.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
usernames = []
if usernames:
    for user in usernames:
        if (user.lower() == "admin"):
            print(f"Hello {user},would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
We need to find some users!
```

</details>

---

### Assignment 5.10 - Checking Usernames

Do the following to create a program that simulates how websites ensure that everyone has a unique username.

* Make a list of five or more usernames called current_users.
* Make another list of five usernames called new_users. Make sure one or two of 
  the new usernames are also in the current_users list.
* Loop through the new_users list to see if each new username has already been 
  used. If it has, print a message that the person will need to enter a new 
  username. If a username has not been used, print a message saying that the 
  username is available.
* Make sure your comparison is case insensitive. If `John` has been used, 
  `JOHN` should not be accepted. (To do this, you'll need to make a copy of 
  current_users containing the lowercase versions of all existing users.)

Solution:

<details>
<summary>Spoiler Code</summary>

```python
current_users = ["Anna", "Bob", "Charlie", "Diana", "Admin"]
lower_case_users = []
for user in current_users:
    lower_case_users.append(user.lower())
new_users = ["abigail", "bob", "curtis", "diana", "edward"]
for user in new_users:
    if (user.lower() in lower_case_users):
        print(f"Sorry. Username {user} is already in use. Choose another username")
    else:
        print(f"Username {user} is available.")
        current_users.append(user.title())
        lower_case_users.append(user.lower())
print("Final list of users:")
print(current_users)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Username abigail is available.
Sorry. Username bob is already in use. Choose another username
Username curtis is available.
Sorry. Username diana is already in use. Choose another username
Username edward is available.
Final list of users:
['Anna', 'Bob', 'Charlie', 'Diana', 'Admin', 'Abigail', 'Curtis', 'Edward']
```

</details>

---

### Assignment 5.11 - Ordinal Numbers

Ordinal numbers indicate their position in a list, such as 1st or 2nd.

Most ordinal numbers end in th, except 1, 2, and 3.
* Store the numbers 1 through 9 in a list.
* Loop through the list.
* Use an if-elif-else chain inside the loop to print the proper ordinal ending 
  for each number. Output should read: `1st 2nd 3rd 4th 5th 6th 7th 8th 9th`, 
  and each result should be on a separate line.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
numerals = list(range(1, 10))
for numeral in numerals:
    if numeral == 1:
        suffix = "st"
    elif numeral == 2:
        suffix = "nd"
    elif numeral == 3:
        suffix = "rd"
    else:
        suffix = "th"
    ordinal = f"{numeral}{suffix}"
    print(ordinal)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
```

</details>

---

### Assignment 5.12 - Styling `if` Statements

Review the programs you wrote in this chapter, and make sure you styled your 
conditional tests appropriately.

For example, Make sure to have one space on either side of comparison operators.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
# No separate code
print("Complete this exercise in your other files.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Complete this exercise in your other files.
```

</details>

---

### Assignment 5.13 - Your Ideas

At this point, you're a more capable programmer than you were when you started 
this book.

* Now that you have a better sense of how real-world situations are modeled in 
  programs, you might be thinking of some problems you could solve with your 
  own programs.
* Record any new ideas you have about problems you might want to solve as your 
  programming skills continue to improve.
* Consider games you might want to write, data sets you might want to explore, 
  and web applications you'd like to create.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
# No separate code
print("Complete this exercise on your own.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Complete this exercise on your own.
```

</details>

---
