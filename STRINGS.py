# Strings are sequences of characters used to store and manipulate text. In Python, strings are enclosed in single
# quotes ('), double quotes ("), triple single quotes ('''), or triple double quotes ("""). They are immutable,
# meaning once a string is created, it cannot be changed.

print("Hello World")

# string operations
# 1) String Concatenation
first_name = "kelvin"
second_name = "njuguna"
full_name = first_name + " " +  second_name
print(full_name)

# 2) Repetition
# you can repeat strings using the *
greet = "Hello"
print(greet * 3)

# 3) indexing and slicing
# access single characters using an index
sample_string = "python"
print(sample_string[0])
print(sample_string[-1])

# slicing a string
sample_string = "python"
print(sample_string[0:4])
print(sample_string[1:4])
print(sample_string[:4])
# the code below is so tricky
print(sample_string[:-1])

# 4) Find the Length of a string using len()
print(len(sample_string))

# 5) String built in methods
text = " hello world "
new_text = text.strip()
print(new_text)

# a)  capitalize() - capitalize the first character of a string
my_name = "kelvin"
new_name = my_name.capitalize()
print(new_name)

# b)  case fold()  - converts a string to lower case..more aggressive than the lower()
my_name = "Kelvin"
new_name = my_name.casefold()
print(new_name)

# c) ends with() - returns true if the string ends with a specific suffix
my_name = "Kelvin Njuguna"
result = my_name.endswith("Njuguna")
print(result)

# d) find() - returns an index of the first occurrence of a substring else returns -1
my_name = "Kelvin Njuguna"
result = my_name.find("o")
if result > 0:
    print("The element is at index: ", result)
else:
    print("Element not found")

# e) format() - used to format specified strings and insert then inside the placeholder denoted using empty curly
# braces, indexes , etc.This returns a formatted string
print("my name is {fname} and i am {age} years old".format(fname = "Kelvin", age = 21))
first_name = str(input("Enter your first name: " ))
second_name = str(input("Enter your second name: "))
my_info = "my first name is {} and second name is {}".format(first_name, second_name)
print(my_info)

# f) index() - similar to find() but raises a Value error if the specified substring or character is not found
my_name = "kelvin njuguna"
position = my_name.index("o")
print(position)

# g) isalphanumeric () - returns true if all characters in the string are alphanumeric
user_password = str(input("Enter a strong password: "))
print(user_password.isalnum())


