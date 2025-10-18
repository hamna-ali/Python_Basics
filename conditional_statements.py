# Example: Using if, elif, and else
language = "Python"

if language == "Python":
    print("The language is Python")
elif language == "Java":
    print("The language is Java")
else:
    print("No match found")


user = "Admin"
logged_in = False

# Using logical AND
if user == "Admin" and logged_in:
    print("Access granted: Admin page")
else:
    print("Access denied: Invalid credentials")

# Using NOT operator
if not logged_in:
    print("Please log in first")
else:
    print("Welcome back!")


# Comparing two lists
a = [1, 2, 3]
b = [1, 2, 3]

# Assigning reference
b = a

# Equality vs identity
print("a == b:", a == b)       # Compares values
print("ID of a:", id(a))
print("ID of b:", id(b))
print("a is b:", a is b)       # Checks if both refer to same object
print("IDs are equal:", id(a) == id(b))


condition = 10  # Non-zero numbers evaluate to True

if condition:
    print("Evaluated as True")
else:
    print("Evaluated as False")
