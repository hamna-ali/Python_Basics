# functions_demo.py

# Define a simple function with no parameters
def greet():
    print("Hello! Welcome to Python functions.")

# Call the function
greet()


# Define a function that takes arguments
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Use the function and print result
result = add(5, 3)
print("add(5, 3) =", result)


# Function with default parameter value
def multiply(x, y=2):
    """Multiplies x by y (default y=2)."""
    return x * y

print("multiply(4) =", multiply(4))
print("multiply(4, 5) =", multiply(4, 5))


# Function with keyword arguments
def describe_person(name, age, city):
    """Prints a description of the person."""
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(name="Alice", age=30, city="Lahore")


# A function that returns multiple values
def min_and_max(numbers):
    """Returns the minimum and maximum of a list of numbers."""
    return min(numbers), max(numbers)

nums = [10, 2, 8, 4, 6]
minimum, maximum = min_and_max(nums)
print("List:", nums)
print("Minimum:", minimum)
print("Maximum:", maximum)


# Using a function inside another function
def square(n):
    return n * n

def sum_of_squares(a, b):
    """Returns square(a) + square(b)."""
    return square(a) + square(b)

print("sum_of_squares(3, 4) =", sum_of_squares(3, 4))


# Demonstrate docstring & introspection
print("Docstring for add():", add.__doc__)


# Function to check if a year is a leap year
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Function to get days in a month
def days_in_month(year, month):
    # Index 0 is a placeholder to match month numbers (1–12)
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for valid month
    if month < 1 or month > 12:
        return "Invalid month. Please enter between 1–12."
    
    # February adjustment for leap year
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]


# --- Program Execution ---
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print(f"Year {year} is a Leap Year? {is_leap(year)}")
print(f"Number of days in month {month}: {days_in_month(year, month)}")
