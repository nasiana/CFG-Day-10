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

