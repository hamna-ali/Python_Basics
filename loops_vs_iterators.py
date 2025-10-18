# -------------------------------
# Example 1: Normal 'for' Loop
# -------------------------------
numbers = [1, 2, 3, 4, 5]

print("➡ Using a normal for-loop:")
for num in numbers:
    print(num)

# Behind the scenes, Python is automatically creating an iterator object
# from 'numbers' and calling next() until StopIteration is raised.

print("\n➡ Doing the same using an iterator manually:")

# -------------------------------
# Example 2: Using Iterators Manually
# -------------------------------

# Convert the list into an iterator object
numbers_iter = iter(numbers)

# Retrieve elements one by one using next()
print(next(numbers_iter))  # 1
print(next(numbers_iter))  # 2
print(next(numbers_iter))  # 3
print(next(numbers_iter))  # 4
print(next(numbers_iter))  # 5

# If we try calling next() again, it will raise StopIteration
# Uncomment below to see the error:
# print(next(numbers_iter))

print("\n➡ Summary:")
print("A 'for' loop automatically calls iter() and next() internally.")
print("An iterator allows you to control iteration manually.")

# -------------------------------
# Example 3: While Loop with Iterator
# -------------------------------
print("\n➡ Using a while loop with an iterator:")
letters = ['a', 'b', 'c']
it = iter(letters)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break  # Stops when no elements are left

# -------------------------------
# Example 4: Demonstrating loop control statements
# -------------------------------
print("\n➡ Loop control example (break and continue):")
for num in numbers:
    if num == 3:
        print("Found 3 — breaking the loop.")
        break
    elif num == 2:
        print("Skipping number 2.")
        continue
    print("Number:", num)
