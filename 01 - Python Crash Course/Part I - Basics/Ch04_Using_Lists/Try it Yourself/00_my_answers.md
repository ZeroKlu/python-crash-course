## Chapter 4 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 4 try-it-yourself exercises.

---

### Assignment 4.1 - Pizzas

Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

* Modify your for loop to print a sentence using the name of the pizza instead 
  of printing just the name  of the pizza. For each pizza you should have one 
  line of output containing a simple statement like:  
  `I like pepperoni pizza.`
* Add a line at the end of your program, outside the for loop, that states how 
  much you like pizza. The output should consist of three or more lines about 
  the kinds of pizza you like and then an additional sentence, such as "I 
  really love pizza!"

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from random import choice

pizzas = ["margherita", "spinach and garlic", "feta and black olive"]
adjectives = ["delicious", "tasty", "scrumptious"]
for pizza in pizzas:
    # print(pizza)
    print(f"I think {pizza} pizza is {choice(adjectives)}!")
print("Pizza is magnificent!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
I think margherita pizza is tasty!
I think spinach and garlic pizza is scrumptious!
I think feta and black olive pizza is delicious!
Pizza is magnificent!
```

</details>

---

### Assignment 4.2 - Animals

Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

* Modify your program to print a statement about each animal, such as "A dog would make a great pet."
* Add a line at the end of your program stating what these animals have in common. You could print a sentence such as "Any of these animals would make a great pet!"

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from random import choice

animals = ["octopus", "squid", "cuttlefish"]
verbs = ["eat", "devour", "dine on"]
for animal in animals:
    print(f"I like to {choice(verbs)} {animal}.")
print("You have to be very careful cooking any of these animals.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
I like to devour octopus.
I like to dine on squid.
I like to eat cuttlefish.
You have to be very careful cooking any of these animals.
```

</details>

---

### Assignment 4.3 - Counting to Twenty

Use a for loop to print the numbers from 1 to 20, inclusive.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
for num in range(1, 21):
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
2
... -- SNIP --
19
20
```

</details>

---

### Assignment 4.4 - One Million

Make a list of the numbers from one to one million, and then use a for loop to 
print the numbers. (If the output is taking too long, stop it by pressing 
`CTRL`+`C` or by closing the output window.)


Solution:

<details>
<summary>Spoiler Code</summary>

```python
million = list(range(1, 1_000_001))
for num in million:
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
2
3
4
5
... -- SNIP --
999996
999997
999998
999999
1000000
```

</details>

---

### Assignment 4.5 - Summing a Million

Make a list of the numbers from one to one million, and then use `min()` and 
`max()` to make sure your list actually starts at one and ends at one million. 
Also, use the `sum()` function to see how quickly Python can add a million 
numbers.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
million = list(range(1, 1_000_001))
print(min(million))
print(max(million))
print(sum(million))
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
1000000
500000500000
```

</details>

---

### Assignment 4.6 - Odd Numbers

Use the third argument of the range() function to make a list of the odd 
numbers from 1 to 20. Use a for loop to print each number.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
nums = list(range(1, 21, 2))
for num in nums:
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
3
5
7
9
11
13
15
17
19
```

</details>

---

### Assignment 4.7 - Threes

Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the 
numbers in your list.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
nums = list(range(3, 31, 3))
for num in nums:
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
3
6
9
12
15
18
21
24
27
30
```

</details>

---

### Assignment 4.8 - Cubes

A number raised to the third power is called a cube. For example, the cube of 
2 is written as 2 ** 3 in Python. Make a list of the first 10 cubes (that is, 
the cube of each integer from 1 through 10), and use a for loop to print out 
the value of each cube.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)
for num in cubes:
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
8
27
64
125
216
343
512
729
1000
```

</details>

---

### Assignment 4.9 - Cube Comprehension

Use a list comprehension to generate a list of the first 10 cubes.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
```

</details>
<br>

<details>
<summary>Output</summary>

```
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

</details>

---

### Assignment 4.10 - Slices

Using one of the programs you wrote in this chapter, add several lines to the 
end of the program that do the following:

* Print the message "The first three items in the list are:"  
  Then use a slice to print the first three items from that program's list.
* Print the message "Three items from the middle of the list are:"  
  Use a slice to print three items from the middle of the list. 
* Print the message "The last three items in the list are:"  
  Use a slice to print the last three items in the list.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
odd_numbers = list(range(1, 21, 2))
print(f"The first three odd numbers are: {odd_numbers[:3]}")
print(f"The next three odd numbers are: {odd_numbers[3:6]}")
print(f"The last three odd numbers are: {odd_numbers[-3:]}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
The first three odd numbers are: [1, 3, 5]
The next three odd numbers are: [7, 9, 11]
The last three odd numbers are: [15, 17, 19]
```

</details>

---

### Assignment 4.11 - My Pizzas, Your Pizzas

Start with your program from Exercise 4-1

Make a copy of the list of pizzas, and call it `friend_pizzas`. Then, do the following:
 
* Add a new pizza to the original list.
* Add a different pizza to the list friend_pizzas.
* Prove that you have two separate lists.
    * Print the message "My favorite pizzas are:" and then use a for loop to 
      print the first list.
    * Print the message "My friend's favorite pizzas are:" and then use a for 
      loop to print the second list.
    * Make sure each new pizza is stored in the appropriate list.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
my_pizzas = ["margherita", "spinach and garlic", "feta and black olive"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("pepperoni")
friend_pizzas.append("sausage and green pepper")

print(f"My favorite pizzas are:")
for pizza in my_pizzas: print(f" - {pizza}")

print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas: print(f" - {pizza}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
My favorite pizzas are:
 - margherita
 - spinach and garlic
 - feta and black olive
 - pepperoni

My friend's favorite pizzas are:
 - margherita
 - spinach and garlic
 - feta and black olive
 - sausage and green pepper
```

</details>

---

### Assignment 4.12 - More Loops

All versions of `foods.py` in this section have avoided using for loops when 
printing to save space. Choose a version of `foods.py`, and write two for 
loops to print each list of foods.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for food in my_foods: print(f" - {food}")
print("\nMy friend's favorite foods are:")
for food in friend_foods: print(f" - {food}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
My favorite foods are:
 - pizza
 - falafel
 - carrot cake
 - cannoli

My friend's favorite foods are:
 - pizza
 - falafel
 - carrot cake
 - ice cream
```

</details>

---

### Assignment 4.13 - Buffet

A buffet-style restaurant offers only five basic foods. Think of five simple 
foods, and store them in a tuple.

* Use a for loop to print each food the restaurant offers.
* Try to modify one of the items, and make sure that Python rejects the change.
* The restaurant changes its menu, replacing two of the items with different 
  foods.

Add a line that rewrites the tuple, and then use a for loop to print each of 
the items on the revised menu.

Solution:

#### Create Tuple

<details>
<summary>Spoiler Code</summary>

**Initial Tuple**

```python
menu = ("sandwich", "pastry", "coffee", "tea", "bagel")
print("Menu:")
for food in menu: print(f" - {food}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Menu:
 - sandwich    
 - pastry      
 - coffee      
 - tea
 - bagel
```

</details>
<br>

#### Try to Edit Tuple

<details>
<summary>Spoiler Code</summary>

```python
Uncomment this line to see immutability error
menu[0] = "toast"
```

</details>
<br>

<details>
<summary>Output</summary>

```
Traceback (most recent call last):
  File "...\13_buffet.py", line 17, in <module>
    menu[0] = "toast"
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

</details>
<br>

#### Replace Tuple

<details>
<summary>Spoiler Code</summary>

```python
menu = ("toast", "pastry", "coffee", "tea", "yoghurt")
print("Updated Menu:")
for food in menu: print(f" - {food}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Updated Menu:
 - toast
 - pastry
 - coffee
 - tea
 - yoghurt
```

</details>

---

### Assignment 4.14 - PEP 8

Look through the original PEP 8 style guide at
[https://python.org/dev/peps/pep-0008](https://python.org/dev/peps/pep-0008).
You won't use much of it now, but it might be interesting to skim through it.

Solution:

<details open>
<summary>Spoiler Code</summary>

```python
# This is a research task - No code needed
# Do this one on your own
```

</details>
<br>

---

### Assignment 4.15 - Code Review

Choose three of the programs you've written in this chapter and modify each one to comply with PEP 8.

* Use four spaces for each indentation level. Set your text editor to insert 
  four spaces every time you press the TAB key, if you haven't already done so 
  (see Appendix B for instructions on how to do this).
* Use less than 80 characters on each line, and set your editor to show a 
  vertical guideline at the 80th character position.
* Don't use blank lines excessively in your program files.

**To set your tab size** to 4 spaces in VS Code (note: it already is at this setting by default):

1. Press `CTRL`+`SHIFT`+`P` to open the menu
2. Enter `settings` in the search and select `Preferences: Open Settings (UI)`
3. Enter `tab size` in the search. Make sure the setting for
   `Editor: Tab Size` is `4`

**To set a guideline** at the 120-character limit

1. Press `CTRL`+`SHIFT`+`P` to open the menu
2. Enter `settings` in the search and select
   `Preferences: Open User Settings (JSON)`
3. At the end of the last item inside the curly-braces, type a comma `,`
4. Add a new line containing the following:  
   `"editor.rulers": [120]`

Note: You can add as many guidelines as you want. e.g.:  
`"editor.rulers": [80, 120]`

Solution:

<details open>
<summary>Spoiler Code</summary>

```python
# Do this one on your own
```

</details>

---
