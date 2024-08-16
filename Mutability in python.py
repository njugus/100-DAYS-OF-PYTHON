# mutability refers to the ability to change the state of objects(data) after the objects are created
# mutable objects can be modified after they are created.
# immutable objects cannot be modified after they are created
# mutable objects - lists, dictionaries, sets, user-defined classes
# immutable objects - integers, float, boolean, tuples, Strings etc

# strings
my_name = "Kelvin"

# integer
my_age = 13
# my_age[0] = 2
# error : TypeError: 'int' object does not support item assignment
# print(my_age)

# lists
my_numbers = [2, 3, 4, 5, 6, 7]
my_numbers[0] = 1
print(my_numbers)
# output : [1, 3, 4, 5, 6, 7]


# interesting fact a) Copying: Mutable: If you assign a mutable object to another variable, both variables reference the
# same object. Changing one will affect the other. Immutable: Since the object cannot be changed, reassigning a
# variable creates a new object, so the original remains unaffected.

# for mutable
my_numbers = [1, 2, 3, 4, 5]
my_list_numbers = my_numbers

my_list_numbers[4] = 8
print(my_numbers)

# output : [1, 2, 3, 4, 8]
# changes made to the second variable affect the first variable coz they refer to the same memory location

# for immutables
# for immutables e.g strings

my_names = "Kelvin Njuguna"

# now note that if you assign immutable variables to other variables you create a new variable
# a new variable means a new memory location
# the changes made to one variable doesn't affect the other
profile_name = my_names
profile_name = "kelvin njuguna kagwima"
print(my_names)




