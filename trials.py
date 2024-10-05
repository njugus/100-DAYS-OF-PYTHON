# example 2

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
