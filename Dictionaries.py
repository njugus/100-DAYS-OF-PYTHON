# how do you create a dictionary

my_details = {
    "name": "Kelvin",
    "email": "kelvin@gmail.com",
    "age": 56,
    "residence": "limuru"
}
# accessing the elements in a dictionary
print(my_details["email"])

# modifying the elements
my_details["profession"] = "FullStackWebDeveloper"

# update an existing value
my_details["residence"] = "Murang'a"

# removing an item from the dictionary
# pop(key) - removes the value of the specified key and returns it
# del dictionary["key"]

removed_value = my_details.pop("age")
print(removed_value)
print(my_details)

# common methods get()- retuns a value and None is the value doesnt exist...None if its set by default otherwise you
# can set the default
print(my_details.get("status"))

# keys - returns a list of keys found in a dictionary
keys = my_details.keys()
for key in keys:
    print(key)

# item() - returns an array of tuples
personal_details = my_details.items()
print(personal_details)
for item in personal_details:
    print(item)

# update() - updates a dictionary with  key-value pairs from another dict or an iterable that contains key-value pairs
additional_details = {
    "marital_status": "Married",
    "spouse": "Ruth Wangui",
    "gender": "male"
}

my_details.update(additional_details)
my_details.update({"is_employed": True})
print(my_details)

# iterating over a dictionary
value = "Kelvin"
for detail in my_details:
    if my_details[detail] == value:
        print("User  Exists in the Database")
        break
else:
    print("User does not exist")

# check whether a key exists in the dictionary
if "age" in my_details:
    print("key exists in the dictionary")
else:
    print("key does not exist in the dictionary")

# dictionary comprehensions
# help you construct dictionaries in a more concise way

squares = {x: x * x for x in range(1, 5)}
print(squares)

# nested Lists

students = {
    "student1": {"name": "Kelvin", "gender": "male", "grade": "B"},
    "student2": {"name": "Ruth", "gender": "female", "grade": "A"},
    "student3": {"name": "George", "gender": "male", "grade": "A"},
    "student4": {"name": "Maryann", "gender": "female", "grade": "B"},
}

for student in students:
    if students[student]["grade"] == "A":
        print(students[student])

# create a function to merge two dictionaries
# Expected output:
# {'a': 1, 'b': 4, 'c': 5, 'd': 6}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}


# use the unpacking operator to merge two dictionaries
# if there is a key in dict1 that matches the key in dict2 then then the key
# in dict 2 overrides the key in dict 1 so the final dict will have the key and value belonging
# to dict 2

def merge_dictionaries(dict1, dict2):
    dict3 = {**dict1, **dict2}
    return dict3


merged_dictionary = merge_dictionaries(dict1, dict2)
print(merged_dictionary)

# you can also use the update()
dict1.update(dict2)
print(dict1)

#  create an inverted dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Expected output:
# {1: 'a', 2: 'b', 3: 'c'}

# method 1
keys = original_dict.keys()
values = original_dict.values()
inverted_dict = {}

# method 2
for key in original_dict:
    inverted_dict.update({original_dict[key] : key})

print(inverted_dict)

# count the frequency of numbers
text = "the quick brown fox jumps over the lazy dog the quick fox"


# Expected output:
# {'the': 3, 'quick': 2, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

def word_count(my_string):
    list_string = my_string.split(" ")
    count_dict = {item: list_string.count(item) for item in list_string}
    return count_dict


print(word_count(text))

# Dictionary comprehension with condition
numbers = [5, 12, 15, 8, 21]

# Expected output:
# {12: 144, 15: 225, 21: 441}

# act on the condition
result = []
for number in numbers:
    if number > 10:
        result.append(number)

# now we can use dictionaries comprehension
square_dict = { item : item * item for item in result}
print(square_dict)
