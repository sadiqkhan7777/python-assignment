# Bitwise Operators
# Used for operations on binary numbers.a value exists in a sequence.

a = 5  # Binary:  0101
b = 3  # Binary:  0011

print(a & b)  # 1  (AND:  0101 & 0011 = 0001)
print(a | b)  # 7  (OR:   0101 | 0011 = 0111)
print(a ^ b)  # 6  (XOR:  0101 ^ 0011 = 0110)
print(~a)     # -6 (NOT:  ~0101 = -(0101+1) = -6)
print(a << 1) # 10 (Left Shift:  0101 << 1 = 1010)
print(a >> 1) # 2  (Right Shift: 0101 >> 1 = 0010)
