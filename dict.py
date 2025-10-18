# Creating a Dictionary
student = {
    "name": "Hamna Ali",
    "age": 22,
    "address": ["Gulshan-e-Ravi", "Lahore"]
}
print("Student Details:", student)
print("Name:", student["name"])
print("Age:", student["age"])

# Accessing data safely using get()
print("Address:", student.get("address"))
print("Country:", student.get("country", "Not Found"))

# Adding a new key-value pair
student["country"] = "Pakistan"
print("After adding country:", student.get("country"))

# Updating existing data
student["age"] = 23
print("After updating age:", student)

# Updating multiple keys at once
student.update({
    "name": "Anum",
    "age": 20,
    "address": ["Model Town", "Lahore"]
})
print("After bulk update:", student)

# Deleting a specific key
del student["age"]
print("After removing age:", student)

# Length of dictionary
print("Number of keys:", len(student))

# Getting only keys, values, and key-value pairs
print("Keys:", student.keys())
print("Values:", student.values())
print("Items (key-value pairs):", student.items())

# Iterating through dictionary
print("\nIterating through keys:")
for key in student:
    print(key)

print("\nIterating through key-value pairs:")
for key, value in student.items():
    print(key, ":", value)
