# Displaying a simple message
print("Hello World")

# Example of using an apostrophe inside single quotes
message = 'It\'s Universe'
print(message)

# Checking the total number of characters in a string
print("Length:", len(message))

# Accessing a specific character using index
print("First character:", message[0])

# Examples of single and double-quoted strings
greet = 'Hello'
planet = "World"
print(greet, planet)

# Example of a multi-line string using triple quotes
para = """This is an
example of a multi-line string."""
print(para)

# Different ways to join strings
combo1 = greet + " " + planet
print("Joined (method 1):", combo1)

combo2 = '{}, {}. Welcome aboard!'.format(greet, planet)
print("Joined (method 2):", combo2)

combo3 = f'{greet}, {planet.upper()}. Welcome aboard!'
print("Joined (method 3):", combo3)

# Exploring common string functions
sample = "  Hello, Python!  "
print("lower():", sample.lower())
print("upper():", sample.upper())
print("count('Hello'):", sample.count('Hello'))

# Finding and replacing text
print("find():", sample.find("Python"))
updated_sample = sample.replace('Python', 'World')
print("replace():", updated_sample)

# Formatting strings using two approaches
username = "Hamna"
user_age = 22

# Using .format() method
formatted1 = "Name: {}, Age: {}".format(username, user_age)
print(formatted1)

# Using f-string formatting (Python 3.6+)
formatted2 = f"Name: {username}, Age: {user_age}"
print(formatted2)
