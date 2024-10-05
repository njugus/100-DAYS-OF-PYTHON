# using the try....except....else...finally blocks
# try - contains the code that may be  bound to an error (risky code)
# except - handles any errors that occur in the try block
# else - if no exceptions occur code inside the else block is excuted(optional)
# finally - code inside this block is executed regardless of whether the exception occureed or not
# this block is used when closing files or connections or releasing resources

# example 1
try:
    result = 10 / 0
except ZeroDivisionError as err:
    print(f"Error : {err}")
else:
    print(result)
finally:
    print("Execution complete")

#Example 2
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError as e:
    print(f"Error : {e}")
except ValueError as e:
    print(f"Error : {e}")
else:
    print(result)
finally:
    print("Execution Complete")



