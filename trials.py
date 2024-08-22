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