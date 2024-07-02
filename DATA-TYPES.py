# we  have 4 data types
# you dont have to define the data type of a variable explicitly
# data type of a variable is inferred from the value

# integer
age = 25

# string
my_name = "kelvin"

# floating point numbers 
average = 45.45656738383

# boolean
is_absent = True
print(age)
print(my_name)
print(average)
print(is_absent)

# use this convention for naming your variables
second_name = "njuguna"
print(second_name)

# you can also use python variables in expressions
first_number = 5
second_number = 6
total_sum = first_number + second_number
print(total_sum)

# you can also concatenate two strings
first_name = "gladys"
second_name = "wanjiru"
full_name = first_name + " " + second_name
print(full_name)

# we can also check the type of variable using the type function
print(type(first_name))
print(type(total_sum))
print(type(average))

# practical example 1
name = "Alice"
age = 25
height = 5.67
is_student = True

print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print("is_student: ", is_student)

# practical example 2
height = 8
width = 4

area = width * height
print(area)
