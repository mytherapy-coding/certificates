# pcep_study_examples.py

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
