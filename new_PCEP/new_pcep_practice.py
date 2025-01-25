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
'''
income = float(input("Enter the annual income: "))

if income < 85528.0:
    tax = (income * 0.18) - 556.2
else:
    tax = (income - 85528.0)*0.32 + 14839.0
if tax < 0:
    tax = 0
tax = round(tax, 00)
print("The tax is:", tax, "thalers")
'''
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


print("""This is a multi-line string.
You can write text on
multiple lines without
using any special characters.""")

for i in range(2, 8):
    print("The value of i is currently", i)

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


import time

'''
# Write a for loop that counts to five.
for i in range(5):
    # Print the iteration number and "Mississippi"
    print(i + 1, "Mississippi")
    time.sleep(1)  # Pause for 1 second

# Print the final message
print("Ready or not, here I come!")

# break - example
print()
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

'''
'''
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

blocks = int(input("Enter the number of blocks: "))

count = 0

for b in range(blocks):
      count += b

      print(count)
        
print("The height of the pyramid:", height)


'''

for i in range(1, 10):
    if i % 2 == 0:
        print(i)

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
print()
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end = "")

print()

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
print()
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

print()
print()
n = 896
digits = []

while n > 0:
    digits.append(n % 10)
    n = n // 10

# Разворачиваем список для прямого порядка
for digit in reversed(digits):
    print("Цифра:", digit)

print()

def print_digits_direct(n):
    if n == 0:
        return
    print_digits_direct(n // 10)
    print("Цифра:", n % 10)

n = 896
print_digits_direct(n)

print("____")

print()
def digits(n: int, base: int = 16):
    # List of possible digits for bases > 10
    digits = "0123456789ABCDEF"
    result = []
    
    while n > 0:
        digit = n % base
        result.append(digits[digit])  # Append the corresponding character
        n //= base
        
    result.reverse()  # Reverse the list to get the correct order
    print(''.join(result))  # Print the result as a string

digits(986)  # This will print the digits of 986 in hexadecimal

print()

def digits(n: int, base: int = 16):
    while n > 0:
        digit = n % base
        print(digit)
        n //= base
        
digits(986)


def digits(n: int, base: int = 10):
    while n > 0:
        digit = n % base
        print(digit)
        n //= base
        
digits(986)

print()

for i in range(1, 11):
    if i % 2 == 1:
      print(i)
print()
x = 1
while x < 11:
    if x % 2 == 0:
        print(x)
    x += 1

print()

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "")

print()

print()

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###
print(numbers[2])
numbers[2] = 1
print(numbers[2])

print()
variable_1 = 1
variable_2 = 2
variable_2 = variable_1
variable_1 = variable_2
print(variable_1)
print(variable_2)

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

print()

for i in range(length // 2):
    print(i)
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
print(length)

print()

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
for x in ("John Lennon", "Paul McCartney", "George Harrison"):
    beatles.append(x)
print("Step 2:", beatles)

# step 3
beatles.append("Stu Sutcliffe")
print("Step 3 :", beatles)

# step 4
del beatles[1]
print("Step 4:", beatles)

# step 5
beatles.insert(2, "Paul McCartney")
print("Step 5:", beatles)


beatles[0] = "----"
print(beatles)

print()
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)
print()
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

print()

my_list = [8, 10, 6, 2, 4]  # list to sort
# It's a little fake, we need it to enter the while loop.

while True:
      swapped = False
      for i in range(len(my_list) - 1):
         if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True  # a swap occurred!
      if not swapped :
            break  # no swaps so far
      
      
print(my_list)
print()
# Copying the entire list.
list_1 = [1]
print(list_1)
list_2 = list_1[:]
print(list_1, list_2)
list_1[0] = 2
print(list_1)
print(list_2)
print()
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
print(my_list[:])
print(my_list[1:3])

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

print()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique = []

for i in range(len(my_list)):
    if my_list[i] not in unique:
        unique.append(my_list[i])

print("The list with unique elements only:", unique)
print(my_list)

print()
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']
vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_one)
print(vehicles_two) # outputs: ['bicycle', 'motor']

del vehicles_two[0]
print(vehicles_one)
print(vehicles_two) # outputs: ['bicycle', 'motor']
print(vehicles_one == vehicles_two)

print()

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2:]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]
print()
row = []

for i in range(8):
    row.append("0")

print(row)

print()

board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
print(board)

i = 2

while i >= 0:
    print("*")
    i -= 2

for i in range(-1, 1):
    print("#")
print()



    
res = [1, 2, 3, 4]

print(res[-3:-2])

for i in range(1):
    print("/")
else:
    print("/")

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
    
print()
t = [[3 - i for i in range(3)] for j in range(3)]
print(t)
s = 0

for i in range(3):
    s += t[i][i]
print(s)

print()

a = 1
b = 0
c = a & b # and 
d = a | b # or
e = a ^ b #!=
print(c + d + e)

print()

a = 1
b = 1
c = a & b 
d = a | b
e = a ^ b
print(c + d + e)

print()

a = 0
b = 0
c = a & b 
d = a | b
e = a ^ b
print(c + d + e)

print()

a = 3 # 11
b = 2 # 10
c = a & b # 11 
          # 10
          # 10 -> 2
d = a | b # 11 
          # 10
          # 11 -> 3

e = a ^ b # 11 
          # 10
          # 01 -> 1


print(c + d + e)
# output 6

print()

a = 3 # 11 - binary, {0, 1} -  et (indexes of bits)
b = 2 # 10 - binary,  {1} - set 
c = a & b # {0, 1} & {1} -> intersect {1} ->  10 -> 2
d = a | b # {0, 1} | {1} -> union {0, 1} -> 11 -> 3
e = a ^ b # {0, 1} ^ {1} -> symetric difference {0} ->  1 -> 1
print(c + d + e)

print()
n = 2**7
print(n)
n = 1 << 7
print(n)
print()


def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

happy_new_year()

print()

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print()
x = boring_function()
print("This lesson is boring...")
print(x)
