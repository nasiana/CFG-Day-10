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

list_comp = [i*i for i in range(1,6) if i % 2 == 0]
print(list_comp)