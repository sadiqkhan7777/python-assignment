# Identity Operators
# Used to compare memory locations of objects.

a = [1, 2, 3]
b = a  # b refers to the same list as a
c = [1, 2, 3]

print(a is b)   # True (Same memory reference)
print(a is c)   # False (Different memory references)
print(a is not c)  # True (a and c are different objects)
