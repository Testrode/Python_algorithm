a = int(5)
b = int(6)

bit_or = a | b
print(bit_or)
bit_and = a & b
print(bit_and)
bit_xor = a ^ b
print(bit_xor)

print(" OR: %s" % bin(bit_or)[2:].zfill(4))
print("AND: %s" % bin(bit_and)[2:].zfill(4))
print("XOR: %s" % bin(bit_xor)[2:].zfill(4))

a = a << 1
print(a)
a = a >> 1
print(a)
