# lists in python
my_fruits = ["apple", "bananas", "guavas", "oranges", "lemon"]

my_fruits.append("lemon")

# lists
my_fruits = ["apple", "bananas", "guavas", "oranges", "lemon"]

# insert an element at a specified index
my_fruits.insert(1, "mangoes")

print(my_fruits)

# lists
my_fruits = ["apple", "bananas", "guavas", "oranges", "lemon"]

# remove an element from a list
my_fruits.remove("lemon")
print(my_fruits)

# lists
my_fruits = ["apple", "bananas", "guavas", "oranges", "lemon"]

# extend this list
# extending the list by adding all the items from an iterable...e.g adding all the items from a list to another list

new_fruits = ["mangoes", "pineapples", "coconut"]

my_fruits.extend(new_fruits)

print(my_fruits)

# pop () does 2 things
# removes returns the last element of a list
# removes the item with the specified index and returns it
print(my_fruits.pop(3))
print(my_fruits)

# index(item)
# returns the index of the first occurrence of the specified item
item = my_fruits.index("apple", 0, 5)
print(item)

# lists
my_fruits = ["apple", "bananas", "apple", "guavas", "oranges", "lemon"]
# count
# returns the number of occurrences of the specified item
print(my_fruits.count("lemon"))

# sorted method
sorted_array = sorted(my_numbers)
print(sorted_array)
print(my_numbers)

# list comprehensions
# used to construct lists in a more friendly manner
my_squares = [x * x for x in range(1, 6)]
print(my_squares)

# lets flatten a 2d list
matrix = [
    [2, 3, 4], [5, 6, 7], [8, 9, 10]
]
flattened_list = [y for x in matrix for y in x]
print(flattened_list)

# comprehension syntax for lists
# [ expression for item in iterable if condition ]
