## Chapter 3 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 3 try-it-yourself exercises.

---

### Assignment 3.1 - Names

Store the names of a few of your friends in a list called names. Print each 
person's name by accessing each element in the list, one at a time.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
friends = ["Matt", "Danica", "Becky", "Alex"]
print(friends[0])
print(friends[1])
print(friends[-2])
print(friends[-1])
```

</details>
<br>

<details>
<summary>Output</summary>

```
Matt
Danica
Becky
Alex
```

</details>

---

### Assignment 3.2 - Greetings

Start with the list you used in Exercise 3.1, but instead of just printing 
each person's name, print a message to them. The text of each message should 
be the same, but each message should be personalized with the person's name.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
print(f"Hi there, {friends[0]}. You're my friend.")
print(f"Hi there, {friends[1]}. You're my friend.")
print(f"Hi there, {friends[-2]}. You're my friend.")
print(f"Hi there, {friends[-1]}. You're my friend.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hi there, Matt. You're my friend.
Hi there, Danica. You're my friend.
Hi there, Becky. You're my friend.
Hi there, Alex. You're my friend.
```

</details>

---

### Assignment 3.3 - Your Own List

Think of your favorite mode of transportation, such as a motorcycle or a car, 
and make a list that stores several examples. Use your list to print a series 
of statements about these items, such as "I would like to own a Honda 
motorcycle."

Solution:

<details>
<summary>Spoiler Code</summary>

```python
cars = ["challenger", "mustang", "camaro"]
print(f"These are some common muscle cars: {cars}")
print(f"The {cars[0]} is my favorite.")
print(f"I like the look of older {cars[1]}s from the 60s and 70s.")
print(f"I don't like the {cars[2]}.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
These are some common muscle cars: ['challenger', 'mustang', 'camaro']
The challenger is my favorite.
I like the look of older mustangs from the 60s and 70s.
I don't like the camaro.
```

</details>

---

### Assignment 3.4 - Guest List

If you could invite anyone, living or deceased, to dinner, who would you 
invite? Make a list that includes at least three people you'd like to invite 
to dinner. Then use your list to print a message to each person, inviting them 
to dinner.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Charles Babbage, would you like to join me for dinner?
Ada Lovelace, would you like to join me for dinner?
George Boole, would you like to join me for dinner?
Grace Hopper, would you like to join me for dinner?
Alan Turing, would you like to join me for dinner?
Tim Berners-Lee, would you like to join me for dinner?
```

</details>

---

### Assignment 3.5 - Changing Guest List

You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.

* Start with your program from Exercise 3-4. Add a print() call at the end of 
  your program stating the name of the guest who can't make it.
* Modify your list, replacing the name of the guest who can't make it with the 
  name of the new person you are inviting.
* Print a second set of invitation messages, one for each person who is still 
  in your list.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"{guests[5]} can't join us for dinner.")
guests[5] = "Linus Torvalds"
print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Tim Berners-Lee can't join us for dinner.
Charles Babbage, would you like to join me for dinner?
Ada Lovelace, would you like to join me for dinner?
George Boole, would you like to join me for dinner?
Grace Hopper, would you like to join me for dinner?
Alan Turing, would you like to join me for dinner?
Linus Torvalds, would you like to join me for dinner?
```

</details>

---

### Assignment 3.6 - More Guests

You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

* Start with your program from Exercise 3-4 or Exercise 3-5.
* Add a `print()` call to the end of your program informing people that you 
  found a bigger dinner table.
* Use `insert()` to add one new guest to the beginning of your list.
* Use `insert() `to add one new guest to the middle of your list.
* Use `append()` to add one new guest to the end of your list.
* Print a new set of invitation messages, one for each person in your list


Solution:

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"I found a bigger table that can seat {len(guests) + 3} people.")
guests.insert(0, "Barbara Liskov")
guests.insert(3, "Donald Knuth")
guests.append("Margaret Hamilton")
print(guests)

print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
print(f"{guests[6]}, would you like to join me for dinner?")
print(f"{guests[7]}, would you like to join me for dinner?")
print(f"{guests[8]}, would you like to join me for dinner?")
```

</details>
<br>

<details>
<summary>Output</summary>

```
['Barbara Liskov', 'Charles Babbage', 'Ada Lovelace', 'Donald Knuth', 'George Boole', 'Grace Hopper', 'Alan Turing', 'Tim Berners-Lee', 'Margaret Hamilton']     
Barbara Liskov, would you like to join me for dinner?
Charles Babbage, would you like to join me for dinner?
Ada Lovelace, would you like to join me for dinner?
Donald Knuth, would you like to join me for dinner?
George Boole, would you like to join me for dinner?
Grace Hopper, would you like to join me for dinner?
Alan Turing, would you like to join me for dinner?
Tim Berners-Lee, would you like to join me for dinner?
Margaret Hamilton, would you like to join me for dinner?
```

</details>

---

### Assignment 3.7 - Shrinking Guest List

You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.

* Start with your program from Exercise 3-6. Add a new line that prints a 
  message saying that you can invite only two people for dinner.
* Use pop() to remove guests from your list one at a time until only two names 
  remain in your list. Each time you pop a name from your list, print a 
  message to that person letting them know you're sorry you can't invite them 
  to dinner.
* Print a message to each of the two people still on your list, letting them 
  know they're still invited.
* Use del to remove the last two names from your list, so you have an empty 
  list.

Print your list to make sure you actually have an empty list at the end of your program.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Barbara Liskov",
    "Charles Babbage",
    "Ada Lovelace",
    "Donald Knuth",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee",
    "Margaret Hamilton"
]

print("Oh no! I can only invite two people to dinner!")
print(f"I'm sorry, {guests.pop(-1)}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop(0)}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"{guests[0]}, you are still invited.")
print(f"{guests[1]}, you are still invited.")
del guests[-1]
del guests[0]
print(guests)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Oh no! I can only invite two people to dinner!
I'm sorry, Margaret Hamilton. I can't invite you to dinner.
I'm sorry, Barbara Liskov. I can't invite you to dinner.
I'm sorry, Tim Berners-Lee. I can't invite you to dinner.
I'm sorry, Alan Turing. I can't invite you to dinner.
I'm sorry, Grace Hopper. I can't invite you to dinner.
I'm sorry, George Boole. I can't invite you to dinner.
I'm sorry, Donald Knuth. I can't invite you to dinner.
Charles Babbage, you are still invited.
Ada Lovelace, you are still invited.
[]
```

</details>

---

### Assignment 3.8 - Seeing the World

Think of at least five places in the world you'd like to visit.

* Store the locations in a list. Make sure the list is not in alphabetical 
  order.
* Print your list in its original order. Don't worry about printing the list 
  neatly, just print it as a raw Python list.
* Use `sorted()` to print your list in alphabetical order without modifying 
  the actual list.
* Show that your list is still in its original order by printing it.
* Use `sorted()` to print your list in reverse alphabetical order without 
  changing the order of the original list.
* Show that your list is still in its original order by printing it again.
* Use `reverse()` to change the order of your list.  
  Print the list to show that its order has changed.
* Use `reverse()` to change the order of your list again.  
  Print the list to show it's back to its original order.
* Use `sort()` to change your list so it's stored in alphabetical order.  
  Print the list to show that its order has been changed.
* Use `sort()` to change your list so it's stored in reverse-alphabetical 
  order.  
  Print the list to show that its order has changed.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
places = ["cairo", "tokyo", "antarctica", "beijing", "australia"]
print(places)

print("---")
print(sorted(places))
print(places)

print("---")
print(sorted(places, reverse = True))
print(places)

print("---")
places.reverse()
print(places)

print("---")
places.reverse()
print(places)

print("---")
places.sort()
print(places)

print("---")
places.sort(reverse = True)
print(places)
```

</details>
<br>

<details>
<summary>Output</summary>

```
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['antarctica', 'australia', 'beijing', 'cairo', 'tokyo']
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['tokyo', 'cairo', 'beijing', 'australia', 'antarctica']
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['australia', 'beijing', 'antarctica', 'tokyo', 'cairo']
---
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['antarctica', 'australia', 'beijing', 'cairo', 'tokyo']
---
['tokyo', 'cairo', 'beijing', 'australia', 'antarctica']
```

</details>

---

### Assignment 3.9 - Dinner Guests

Working with one of the programs from Exercises 3-4 through 3-7, use `len()` to
print a message indicating the number of people you are inviting to dinner.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"I am inviting {len(guests)} people to dinner.")
```

</details>
<br>

<details>
<summary>Output</summary>
Output:

```
I am inviting 6 people to dinner.
```

</details>

---

### Assignment 3.10 - Every Function

Think of something you could store in a list. For example, you could make a 
list of mountains, rivers, countries, cities, languages, or anything else 
you'd like. Write a program that creates a list containing these items and 
then uses each function introduced in this chapter at least once.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
# This is intentionally incomplete
print("You're encouraged to do this one on your own.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
You're encouraged to do this one on your own.
```

</details>

---

### Assignment 3.11 - Intentional Error

If you haven't received an index error in one of your programs yet, try to 
make one happen. Change an index in one of your programs to produce an index 
error. Make sure you correct the error before closing the program.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(guests[6])
```

</details>
<br>

<details>
<summary>Output</summary>

```
Traceback (most recent call last):
  File "...\11_intentional_error.py", line 12, in <module>
    print(guests[6])
          ~~~~~~^^^
IndexError: list index out of range
```

</details>

---
