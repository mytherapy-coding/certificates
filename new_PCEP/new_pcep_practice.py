# Module 1

print("My name is", "Python.", end=" ")
print("My name is", "Python.")
print("My name is", "Python", end="\n")
print("My name is", "Python", end="! ")
print("My name is", "Python.")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print()
print("H", "E", "L", "L", "O", sep="-")

print(11_111_111)
print(0o123)
# The number 123 is interpreted as an octal number due to the 0o prefix.
# To convert it to decimal (base 10), you expand it as follows:
#
# 123 (octal) = 1 × 8^2 + 2 × 8^1 + 3 × 8^0
#             = 1 × 64 + 2 × 8 + 3 × 1
#             = 64 + 16 + 3
#             = 83 (decimal)
#
# Example:
print(0o123)  # Outputs: 83

"""
0x123 is a hexadecimal number (base 16).

If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.

In hexadecimal:
- The prefix "0x" indicates that the number is in base 16.
- The digits range from 0-9 and A-F, where A = 10, B = 11, ..., F = 15.

To convert 0x123 to decimal (base 10):

0x123 = 1 × 16^2 + 2 × 16^1 + 3 × 16^0
      = 1 × 256 + 2 × 16 + 3 × 1
      = 256 + 32 + 3
      = 291 (decimal)
"""
print(0x123)

print(0.0000000000000000000001)

print('I\'m Monty Python.')
print("I'm Monty Python.")

# Binary System
# The binary system is a number system that uses 2 as its base.
# It consists only of the digits 0 and 1, which are called binary digits or bits.

# Example: Converting a Binary Number to Decimal
# Let's consider the binary number "1010" and convert it to decimal (base 10).
# To convert a binary number to decimal, you expand it as follows:

# 1010 (binary) = 1 × 2^3 + 0 × 2^2 + 1 × 2^1 + 0 × 2^0
#               = 1 × 8 + 0 × 4 + 1 × 2 + 0 × 1
#               = 8 + 0 + 2 + 0 = 10 (decimal)

# Therefore, the binary number 1010 is equal to 10 in decimal.

# Code Example: Converting Binary to Decimal in Python
binary_number = "1010"
decimal_number = int(binary_number, 2)
print(decimal_number)  # Outputs: 10
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)


print(-6 // 4)
print(6. // -4)
print("------------------------------")
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(2 ** 2 ** 3)

x =  1
x = float(x)
y = 3*x**3-2*x**2 + 3*x - 1
print("y =", y)

a = 6
b = 3
a /= 2 * b
print(a)
print(15**2.0)
print("\nThat's all, folks!")
'''
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Calculate the total minutes after the duration
total_minutes = (hour * 60) + mins + dura

# Convert back to hours and minutes
end_hour = (total_minutes // 60) % 24  # Use modulo 24 to wrap around if it goes past midnight
end_min = total_minutes % 60

# Display the final time
print(f"The event will end at: {end_hour:02}:{end_min:02}")
x = input("Enter a number: ") # The user enters 2
print(type(x))
'''

# Module 2

print(2 == 2.)


var = 0  # Assigning 0 to var
print(var == 0)

