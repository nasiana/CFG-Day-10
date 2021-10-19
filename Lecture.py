# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# EX 1
clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]
if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'
print(clothes)

# EX 2
our_list = [8, 200, 3, 6, 49, 76, 89, 43, 60, 29]
print(len(our_list))
print(max(our_list))
print(min(our_list))
# literally reverses the order the list is in
print(list(reversed(our_list)))
print(sorte  d(our_list))
print(sorted(our_list, reverse=True))

# EX 3

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for i in costs:
    total_cost += i

 # EX 4
# Write a list comprehension expression to build a new list that calculates the square for the number\
# that are divisible by 2 in range(1, 6). Your sample output should be [4, 16]

# * performs multiplication
list_comp = [i*i for i in range(1,6) if i % 2 == 0]
# or like this, ** to do to the power of something so 2**3 = 8
list_comp_2 = [i**2 for i in range(1,6) if i % 2 == 0]
print(list_comp)
print(list_comp_2)

# EX 5
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
for i in fruits:
# use i to refer back to the dictionary (each iterable represents an individual dictionary)
# it is not a nested dictionary hence dont put the [] consecutively after one another\
# separate the key-value pairs by a comma as this is not a nested dictionary
    print(i['name'], i['colour'], i['price'])

### EXERCISE 1 ###
"""
When I'm travelling in the winter I often forget to pack warm clothes. 
Let's write a program to help me to remember the right clothes.

The program should check if the first item in the clothes list is "shorts". 
If it is it should change the value to "warm coat".
"""

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]
if clothes[0] == "shorts":
    clothes[0] = "warm coat"

print(clothes)

### EXERCISE 2 ###
"""
Make a list of game scores. Using list functions write code to output information of the scores in the following format:

    Number of scores: 10
    Highest score: 200
    Lowest score: 3

Extension: Output all of the scores in descending order
"""

our_list = [8, 200, 3, 6, 49, 76, 89, 43, 60, 29]

print(len(our_list))
print(max(our_list))
print(min(our_list))

print(sorted(our_list, reverse=True))

### Exercise 3
"""
I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.
Write a program that uses a for loop to calculate the total cost
"""
# Example Solution - with for loop
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost = total_cost + cost

print(total_cost)
print("{:.2f}".format(total_cost))

# There is an easier way to do the last program without a for loop.
# The sum() function can be used to add up all of the values in a list:

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total = sum(costs)

print("{:.2f}".format(total))

### Exercise 4
"""
Write a list comprehension expression to build a new list that calculates the square for the number that are divisible by 2 in range(1, 6). 

Your sample output should be ```[4, 16]```
"""

our_new_list = [x * x for x in range(1, 6) if x % 2 == 0]
print(our_new_list)

### Exercise 5
"""
Using a for loop, output the values name, colour and price of each dictionary in the list
"""

fruits = [
    {"name": "apple", "colour": "red", "price": 0.12},
    {"name": "banana", "colour": "yellow", "price": 0.2},
    {"name": "pear", "colour": "green", "price": 0.19},
]

for fruit in fruits:
    print("{} {} {}".format(fruit["name"], fruit["colour"], fruit["price"]))

### Tuples vs Lists - When to use?
"""
- Use lists for collections you may want to change and that you don't know the size of
- Use tuples for collections that should stay the same or have discrete set of values
- Prefer using tuples when the data type of items is different or you are representing a concrete concept (e.g coordinates)
- Prefer using lists when the data is of the same data type
"""

### Summary
"""
List > Mutable collection of items with an unbounded length
Dictionary > Collection of key value pairs 
Tuples > Immutable collection of items with a bounded length 
Set > Collection of unique items 
"""