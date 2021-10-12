# ex 1

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]

if clothes[0] == "shorts":
    clothes[0] = "warm coat"

print(clothes)

# ex 2

our_list = [8, 200, 3, 6, 49, 76, 89, 43, 60, 29]

print(len(our_list))
print(max(our_list))
print(min(our_list))

print(sorted(our_list, reverse = True))

# ex 3

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for i in costs:
    total_cost = total_cost + i

# {:.2f} formats it so the result is rounded to 2 decimal places
print("{:.2f}".format(total_cost))

# another way

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = sum(costs)

# {:.2f} formats it so the result is rounded to 2 decimal places
print("{:.2f}".format(total_cost))

# ex 5

in range(1, 6).

new_list = [ expression for item in list if conditional ]

new_list = [ i**2 for i in range(1, 6) if i % 2 == 0 ]
print(new_list)