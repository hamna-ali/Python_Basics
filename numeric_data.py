# Working with integers (whole numbers)
num1 = 10
num2 = 3
print("num1:", num1)
print("num2:", num2)

# Working with floating-point numbers (decimals)
num3 = 10.5
num4 = 3.2
print("num3:", num3)
print("num4:", num4)

# Performing basic arithmetic operations
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division (no remainder):", num1 // num2)
print("Remainder:", num1 % num2)
print("Exponentiation:", num1 ** num2)

# Combining integers and floats in an expression
mixed_result = num1 + num3
print("Mixed Result:", mixed_result, "Data Type:", type(mixed_result))

# Common built-in math functions
value = -7.9
print("Absolute Value:", abs(value))
print("Rounded (no decimal):", round(value))
print("Rounded (1 decimal):", round(value, 1))

# Operator precedence (BODMAS rule)
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# Comparison operators (return True or False)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 > num2:", num1 > num2)
print("num2 < num1:", num2 < num1)
print("num1 >= 10:", num1 >= 10)
print("num2 <= 3:", num2 <= 3)

# String vs numeric addition
n1 = '100'
n2 = '200'
print("String Concatenation:", n1 + n2)

# Type casting (converting strings to integers)
n1 = int(n1)
n2 = int(n2)
print("Numeric Addition:", n1 + n2)
