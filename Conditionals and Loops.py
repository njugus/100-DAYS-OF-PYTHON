# Write a program that checks if a number is positive, negative, or zero.

def check_number(num):
    if num < 0:
        print("The number is a negative number")
    elif num == 0:
        print("The number is zero")
    else:
        print("The number is a positive number")


# Write a program that checks if a number is positive and even, or positive and odd.
def check_positive_and_even(num):
    if num >= 0 and num % 2 == 0:
        print("The number is both positive and even")
    else:
        print("The number is both positive and odd")


# Write a program that grades a student based on their score.
def grade_students(score):
    if score >= 80:
        print("A")
    elif score >= 70:
        print("B")
    elif score >= 40:
        print("C")
    else:
        print("D")


# Write a program that prints all even numbers from 1 to 10.
for i in range(1, 11):
    print(i)


# a program that prints even numbers from 1 to 10
def check_even_numbers():
    for num in range(1, 11):
        if num % 2 == 0:
            print(num)


# a program that prints odd numbers from 1 to 10
def check_odd_numbers():
    for num in range(1, 11):
        if num % 2 != 0:
            print(num)


# find the sum of all even numbers between 1 and 100


def find_even_numbers(limit):
    even_numbers = []
    for number in range(1, limit):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def find_sum(numbers):
    sum = 0
    for even_number in numbers:
        sum += even_number

    return sum


result = find_even_numbers(100)
print(result)
print(find_sum(result))


# program to find the factorial of a number
# factorial - result of multiplying the number with all numbers below it
# 5! = 5 * 4 * 3 * 2 * 1
# input - number
# for loop
# output - factorial of the number

def find_factorial(number):
    factor = 1
    for i in range(2, number + 1):
        factor = factor * i
    return factor


# count the number of vowels in a string ignoring capitalization
# input - a string
# process
# output - count variable

vowels_set = {"a", "e", "i", "o", "u"}


def find_vowels(my_string):
    count = 0
    new_string = my_string.lower()
    for x in new_string:
        for y in vowels_set:
            if x == y:
                count += 1
                break
    return count

