# 🔹 Python Data Types (with Examples)
                                                                            # 1. Numeric Types

# Integer (int)
# x = 10
# print(type(x))  # Output: <class 'int'>

# Floating-point (float)
# y = 3.14
# print(type(y))  # Output: <class 'float'>

# Complex number (complex)
# z = 2 + 3j
# print(type(z))  # Output: <class 'complex'>

                                                                            # 2. Sequence Types
# String (str)
# text = "Hello, Python!"
# print(type(text))  # Output: <class 'str'>

# List (list) - Mutable ordered collection
# my_list = [1, 2, 3, "Python"]
# print(type(my_list))  # Output: <class 'list'>

# Tuple (tuple) - Immutable ordered collection
# my_tuple = (1, 2, 3, "Python")
# print(type(my_tuple))  # Output: <class 'tuple'>

# Range (range) - Sequence of numbers
# my_range = range(5)  # Generates numbers from 0 to 4
# print(type(my_range))  # Output: <class 'range'>

                                                                            # 3. Set Types
# Set (set) - Unordered collection with unique elements
# my_set = {1, 2, 3, 3, 2}
# print(type(my_set))  # Output: <class 'set'>
# print(my_set)  # Output: {1, 2, 3}

# Frozenset (frozenset) - Immutable version of a set
# frozen = frozenset([1, 2, 3])
# print(type(frozen))  # Output: <class 'frozenset'>

                                                                            # 4. Mapping Types
# Dictionary (dict) - Key-value pairs
# my_dict = {"name": "Alice", "age": 25}
# print(type(my_dict))  # Output: <class 'dict'>

                                                                            # 5. Boolean Type
# Boolean (bool) - True or False
# is_active = True
# print(type(is_active))  # Output: <class 'bool'>

                                                                            # 6. Binary Types
# Bytes (bytes) - Immutable byte sequence
# my_bytes = b"hello"
# print(type(my_bytes))  # Output: <class 'bytes'>

# Bytearray (bytearray) - Mutable byte sequence
# my_bytearray = bytearray(5)  # Creates byte array of size 5
# print(type(my_bytearray))  # Output: <class 'bytearray'>

# Memoryview (memoryview) - Memory-efficient byte handling
# mv = memoryview(b"Python")
# print(type(mv))  # Output: <class 'memoryview'>

                                                                            # 7. None Type
# NoneType (None) - Represents the absence of a value
# nothing = None
# print(type(nothing))  # Output: <class 'NoneType'>

# 🔹 Python Special Keywords (with Examples)
                                                                            # 1. Control Flow Keywords

# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
#  'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
#  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', 
#  'match', 'case']


# x = 10

# # if, elif, else
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is 5")
# else:
#     print("x is less than 5")

# # for loop
# for i in range(3):
#     print("Loop:", i)

# # while loop
# count = 0
# while count < 3:
#     print("Count:", count)
#     count += 1

# # break, continue, pass
# for i in range(5):
#     if i == 2:
#         break  # Stops the loop
#     if i == 1:
#         continue  # Skips this iteration
#     print("i:", i)


                                                                            # 2. Exception Handling Keywords
# try:
#     num = 10 / 0  # Will cause ZeroDivisionError
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# finally:
#     print("This runs no matter what.")

# # assert - Used for debugging
# x = 5
# assert x > 0, "x should be positive"

                                                                                # 3. Function & Class Keywords
# def - Define a function
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))

# # lambda - Anonymous function
# square = lambda x: x * x
# print(square(5))

# # class - Define a class
# class Person:
#     def __init__(self, name):
#         self.name = name

# p = Person("Alice")
# print(p.name)

                                                                                # 4. Variable Handling Keywords
# global - Access global variables inside a function
# x = 10

# def modify():
#     global x
#     x = 20

# modify()
# print(x)  # Output: 20

# # nonlocal - Modify variables from an enclosing scope
# def outer():
#     y = 5
#     def inner():
#         nonlocal y
#         y = 10
#     inner()
#     print(y)

# outer()  # Output: 10

# # del - Delete a variable or object
# z = 100
# del z  # Now z is deleted

                                                                        # 5. Boolean & None Keywords
# True, False - Boolean values
# print(True and False)  # Output: False
# print(not True)  # Output: False

# # None - Represents a null value
# value = None
# print(value)  # Output: None

                                                                        # 6. Import & Module Keywords

# import - Importing a module
# import math
# print(math.sqrt(16))  # Output: 4.0

# # from, as - Importing specific part of a module
# from math import pi as circle_pi
# print(circle_pi)  # Output: 3.141592653589793

# # with - Used in resource management
# with open("example.txt", "w") as file:
#     file.write("Hello, world!")  # File is auto-closed

                                                                        # 7. Object-Oriented Programming Keywords

# is - Identity comparison
# a = [1, 2, 3]
# b = a
# print(a is b)  # Output: True

# # in - Membership test
# print(2 in [1, 2, 3])  # Output: True

# # not, and, or - Logical operators
# print(not False)  # Output: True
# print(True and False)  # Output: False
# print(True or False)  # Output: True

# 8. Asynchronous Programming Keywords

                                                                        # import asyncio

# # async, await - Define asynchronous functions
# async def my_async_function():
#     print("Start")
#     await asyncio.sleep(1)
#     print("End")

# asyncio.run(my_async_function())

                                                                        # 9. Special Keywords

# match, case - Pattern matching (Python 3.10+)
# value = 2
# match value:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")  # Output: Two
#     case _:
#         print("Unknown number")
