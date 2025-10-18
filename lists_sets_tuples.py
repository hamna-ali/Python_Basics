# Working with Lists
fruits = ["apple", "banana", "cherry"]
print("List of Fruits:", fruits)

# Finding the total number of elements
print("Total fruits:", len(fruits))

# Accessing list items using indexing and slicing
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Fruits from index 1 onwards:", fruits[1:])

# Adding new items
fruits.append("date")
print("After append:", fruits)

fruits.insert(0, "banana")
print("After insert at beginning:", fruits)

# Merging two lists
extra_fruits = ["pineapple", "mango"]
fruits.extend(extra_fruits)
print("After extending list:", fruits)

# Removing elements
fruits.remove("apple")
print("After removing 'apple':", fruits)

fruits.pop()
print("After popping last item:", fruits)

# Sorting elements
fruits.sort()
print("Sorted list:", fruits)
fruits.sort(reverse=True)
print("Reverse sorted list:", fruits)

# Using max and min functions
print("Alphabetically last fruit:", max(fruits))
print("Alphabetically first fruit:", min(fruits))

# Lists are mutable — values can be changed
fruits[1] = "blueberry"
print("After modification:", fruits)

# Looping through list elements
print("\nLoop through list:")
for fruit in fruits:
    print("Fruit:", fruit)

print()
for i, fruit in enumerate(fruits):
    print(i, fruit)

print()
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# Joining and splitting list elements
sentence = " - ".join(fruits)
new_list = sentence.split(" - ")
print("\nJoined string:", sentence)
print("Back to list:", new_list)



#SETS
# Working with Sets
nums = {1, 2, 3, 2, 1}
print("Unique Numbers:", nums)

# Checking membership
print("Is 1 present in set?", 1 in nums)

# Performing set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Set a:", a)
print("Set b:", b)
print("Union (a ∪ b):", a.union(b))
print("Intersection (a ∩ b):", a.intersection(b))
print("Difference (a - b):", a.difference(b))

print()

# Declaring empty collections
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()  # Correct way to create an empty set
print("Empty set created:", empty_set)


# Working with Tuples

# Understanding Mutable vs Immutable types

# Mutable (List Example)
colors = ["red", "green", "blue"]
print("Original List:", colors)

copy_colors = colors
print("Copied List:", copy_colors)

colors[0] = "purple"
print("After modification (original):", colors)
print("After modification (copy):", copy_colors)

# Immutable (Tuple Example)
tuple_colors = ("red", "green", "blue")
print("\nOriginal Tuple:", tuple_colors)

# Attempting to modify a tuple will cause an error
# tuple_colors[0] = "purple"  # ❌ This is not allowed
# print(tuple_colors)
