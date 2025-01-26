# Module 1

The string is **<span style="color: red;">delimited</span>** with quotes - in fact, the quotes make the string - they cut out a part of the code and assign a different meaning to it.

**<span style="color: red;">invoke</span>** typically means to call or execute a function



## Integers: octal and hexadecimal numbers

* In Python, numbers prefixed with 0o (zero followed by a lowercase "o") are interpreted as octal numbers (base 8).
* Octal numbers use digits 0-7.

The number 123 is interpreted as an <span style="color: red;">octal number</span> due to the 0o prefix.
To convert it to decimal (base 10), you expand it as follows:

123 (octal) = 1 × 8^2 + 2 × 8^1 + 3 × 8^0
            = 1 × 64 + 2 × 8 + 3 × 1
            = 64 + 16 + 3
            = 83 (decimal)


## 0x123 is a hexadecimal number (base 16).

If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only. 

In <span style="color: red;">hexadecimal number</span>:
- The prefix "0x" indicates that the number is in base 16.
- The digits range from 0-9 and A-F, where A = 10, B = 11, ..., F = 15.

To convert 0x123 to decimal (base 10):

0x123 = 1 × 16^2 + 2 × 16^1 + 3 × 16^0
      = 1 × 256 + 2 × 16 + 3 × 1
      = 256 + 32 + 3
      = 291 (decimal)

A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34.

6.62607E-34

print(0.0000000000000000000001) 
outcome 1e-22


## Binary System
The binary system is a number system that uses 2 as its base.
It consists only of the digits 0 and 1, which are called binary digits or bits.

Example: Converting a <span style="color: red;">Binary Number</span> to Decimal
Let's consider the binary number "1010" and convert it to decimal (base 10).
To convert a binary number to decimal, you expand it as follows:

1010 (binary) = 1 × 2^3 + 0 × 2^2 + 1 × 2^1 + 0 × 2^0
              = 1 × 8 + 0 × 4 + 1 × 2 + 0 × 1
              = 8 + 0 + 2 + 0 = 10 (decimal)

Therefore, the binary number 1010 is equal to 10 in decimal.
"""

binary_number = "1010"
decimal_number = int(binary_number, 2)
print(decimal_number)  # Outputs: 10

## Basic operators
Data and operators when connected together form expressions. The simplest expression is a literal itself.


Integer division can also be called floor division.  

A // (double slash) sign is an integer divisional operator. It differs from the standard / operator in two details:

its result lacks the fractional part - it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded;
it conforms to the integer vs. float rule.

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)


print(-6 // 4)
print(6. // -4)


Note: some of the values are negative. This will obviously affect the result. But how?

The result is two negative twos. The real (not rounded) result is -1.5 in both cases. However, the results are the subjects of rounding. <span style="color: red;">The rounding goes toward the lesser integer value, and the lesser integer value is -2, hence: -2 and -2.0.</span>

## Operators: remainder (modulo)
The result of the operator is a remainder left after the integer division.

In other words, it's the value left over after dividing one value by another to produce an integer quotient.

Note: the operator is sometimes called modulo in other programming languages.

Take a look at the snippet - try to predict its result and then run it:

print(14 % 4)


As you can see, the result is two. This is why:

14 // 4 gives 3 → this is the integer quotient;
3 * 4 gives 12 → as a result of quotient and divisor multiplication;
14 - 12 gives 2 → this is the remainder.


A <span style="color: red;">unary operator</span> is an operator with only one operand, e.g., -1, or +3.

A <span style="color: red;">binary operator</span> is an operator with two operands, e.g., 4 + 5, or 12 % 5.

## Operator Precedence
In Python, the exponentiation operator (**) has <span style="color: yellow;">right-to-left associativity</span>. This means that when you have multiple ** operators in a row, Python evaluates them from right to left.
Thus, the expression 2 ** 2 ** 3 is evaluated as:

scss
Copy code
2 ** (2 ** 3)

## Solving simple mathematical problems
Now you should be able to construct a short program solving simple mathematical problems such as the Pythagorean theorem:

The square of the hypotenuse is equal to the sum of the squares of the other two sides.

The following code evaluates the length of the hypotenuse (i.e., the longest side of a right-angled triangle, the one opposite of the right angle) using the Pythagorean theorem:

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)


Note: we need to make use of the ** operator to evaluate the square root as:

√ (x)  = x(½)

and

c = √ a2 + b2 

<span style="color: red;">The input() function in Python always returns a string (even if you type a number).</span>

# Module 2

## Inequality: the not equal to operator (!=)

var = 0  # Assigning 0 to var 

print(var != 0)

```py
var = 0  # Assigning 0 to var
print(var != 0)
```

```py
n = int(input("Enter a number: " ))
print(n >= 100)

plant = input("Enter a plant: ")
```

```py
if plant == "Spathiphyllum":
    print("Spathiphyllum is the best plant ever!")
else:
    print("not the best plant")
```
*If the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.
It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.*

```py
income = float(input("Enter the annual income: "))

if income < 85528.0:
    tax = (income * 0.18) - 556.2
else:
    tax = (income - 85528.0)*0.32 + 14839.0
if tax < 0:
    tax = 0
tax = round(tax, 00)
print("The tax is:", tax, "thalers")
```
*Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.*

```py
year = int(input("Enter a year: "))

if year >= 1582:
    
    if year%4 == 0 or year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0:
        print("Leap year")
    else:
        print("Common year")

else: 
    print("Not within the Gregorian calendar period")
```

## While Loop

```py
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
```

*A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
Your task is to help the magician complete the code in the editor in such a way so that the code:
will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."*

```py
secret_number = 777

number = int(input("Enter the number: "))
while True:
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        number = int(input("Try again: "))  # Prompt the user to guess again
    else:
        print("Well done, muggle! You are free now.")
        break  # Exit the loop
```

## For Loop

```py
import time
# Write a for loop that counts to five.
for i in range(5):
    # Print the iteration number and "Mississippi"
    print(i + 1, "Mississippi")
    time.sleep(1)  # Pause for 1 second

# Print the final message
print("Ready or not, here I come!")
```
The purpose of time.sleep(1) in the given code is to create a pause of 1 second between each iteration of the loop. 

*The break statement is used to exit/terminate a loop.
Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.*

```py
secret_word = "chupacabra"

while True:
    word = input("Enter a word: ")
    if word == secret_word:
        print("You've successfully left the loop.")
        break  
```

*The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
It can be used with both the while and for loops.
Your task here is very special: you must design a vowel eater! Write a program that uses:
a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:
ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.*

```py
user_word = input("Enter a word: ")
user_word = user_word.upper()  # Convert the input to uppercase
print(user_word)

for letter in user_word:
    # Check if the letter is a vowel (A, E, I, O, U)
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue  # Skip vowels
    print(letter)
```
```py
word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    word_without_vowels += letter
    # Complete the body of the loop.
print(word_without_vowels)

# Print the word assigned to word_without_vowels.
```

## The while loop and the else branch

Loops may have the else branch too, like ifs.

The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.

```py
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
```
For loops behave a bit differently - take a look at the snippet in the editor and run it.
The output may be a bit surprising.
The i variable retains its last value.
Modify the code a bit to carry out one more experiment.

```py
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
```
*Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:
Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.*


```py
# Input: total number of blocks
blocks = int(input("Enter the number of blocks: "))

height = 0
used_blocks = 0

# Keep adding layers while there are enough blocks
while True:
    height += 1
    used_blocks += height  # Add blocks for the current layer
    
    # Check if the next layer exceeds the number of available blocks
    if used_blocks > blocks:
        height -= 1  # Undo the last layer addition as it wasn't completed
        break

# Output the height of the pyramid
print("Height of the pyramid:", height)
```
Scenario
In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.

Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.


Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

```py
# Read the initial number from the user
c0 = int(input("Enter a natural number: "))

# Initialize the step counter
steps = 0

# Print the initial value
print(c0)

# Continue the process until c0 becomes 1
while c0 != 1:
    # If the number is even, divide it by 2
    if c0 % 2 == 0:
        c0 = c0 // 2
    # If the number is odd, multiply by 3 and add 1
    else:
        c0 = 3 * c0 + 1
    
    # Print the current value of c0
    print(c0)
    
    # Increment the step counter
    steps += 1

# Output the total number of steps
print("Steps:", steps)
```

```py
# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
```
## Bitwise operators
- & (ampersand) - bitwise conjunction; AND
- | (bar) - bitwise disjunction; OR
- ~ (tilde) - bitwise negation; - NOT
- ^ (caret) - bitwise exclusive or (xor). - Bitwise XOR (Exclusive OR)

## Number systems or bases
- 2 — binary
- 8 — octal
- 10 — decimal  
- 16 — hexadecimal 

```py
def digits(n: int, base: int = 10):
    while n > 0:
        digit = n % base
        print(digit)
        n //= base
        
digits(986)
```
## Binary Conversion 

```py
def to_binary(num):
    if num == 0:
        return '0'  # Handle the special case for 0
    binary = ''
    while num > 0:
        binary += str(num % 2)
        num //= 2
    return binary[::-1]

```
## Base <= 10

```py
def to_base(num, base):
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result += str(num % base)  # Directly convert remainder to a string
        num //= base
    return result[::-1]
```

## Base >10

```py
def to_base(num, base):
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        remainder = num % base
        if remainder < 10:
            result += str(remainder)  # For 0-9, convert directly to string
        else:
            result += chr(remainder - 10 + ord('A'))  # Map 10+ to 'A', 'B', etc.
        num //= base
    return result[::-1]
```


![alt text](image.png)

![alt text](<PNG image.png>)

## Explanation of Set Operations: Intersection, Union, Difference, and Symmetric Difference

### 1. Intersection

The intersection of two sets includes elements that are common to both sets.

```py
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a & set_b  # Intersection
print(result)  # Output: {3}
```
* Set A: {1, 2, 3}
* Set B: {3, 4, 5}
* A ∩ B (Intersection): {3}


### 2. Union (|)

The union of two sets includes all elements from both sets, with no duplicates.

```py
# Example
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a | set_b  # Union
print(result)  # Output: {1, 2, 3, 4, 5}
```
* Set A: {1, 2, 3}
* Set B: {3, 4, 5}
* A ∪ B (Union): {1, 2, 3, 4, 5}

### 3. Difference (-)
The difference of two sets includes elements that are in the first set but not in the second.

```py
# Example
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a - set_b  # Difference
print(result)  # Output: {1, 2}
```
* Set A: {1, 2, 3}
* Set B: {3, 4, 5}
* A - B (Difference): {1, 2}

### 4. Symmetric Difference (^)
The symmetric difference includes elements that are in either set but not in both (unique elements from each set).

```py
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a ^ set_b  # Symmetric Difference
print(result)  # Output: {1, 2, 4, 5}
```
* Set A: {1, 2, 3}
* Set B: {3, 4, 5}
* A ⊕ B (Symmetric Difference): {1, 2, 4, 5}

To implement bitwise operations using set operations, we first convert integers 
𝑥
x and 
𝑦
y into sets of their binary 1 positions. Using these sets, we perform the desired set operations to mimic bitwise behavior. Here's how the implementation looks:

```py
def int_to_bitset(n: int) -> set:
    """
    Convert an integer to a set of indices where bits are 1.
    """
    return {i for i in range(n.bit_length()) if (n >> i) & 1}

def bitset_to_int(bitset: set) -> int:
    """
    Convert a set of indices back to an integer.
    """
    return sum(1 << i for i in bitset)

def and_operation(x: int, y: int) -> int:
    set_x = int_to_bitset(x)  # Convert x to set of '1' bit indices
    set_y = int_to_bitset(y)  # Convert y to set of '1' bit indices
    set_z = set_x & set_y     # Perform set intersection (AND operation)
    z = bitset_to_int(set_z)  # Convert the resulting set back to integer
    return z
```
```py 
x = 10  # Binary: 1010
y = 12  # Binary: 1100

result = and_operation(x, y)  # Perform bitwise AND
print(result)  # Output: 8 (Binary: 1000)
```

Extending to Other Bitwise Operations
You can generalize this approach for OR, XOR, and NOT using other set operations:

- OR (|): Use set union.
- XOR (^): Use symmetric difference.
- NOT (~): Calculate all possible bit positions (based on bit length) and subtract the existing positions.

## Why do we need lists?

If you do something like this, you would lose the value previously stored in variable_2. Changing the order of the assignments will not help. You need a third variable that serves as an auxiliary storage.

```py
variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
```
```py
variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
```

```py
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
```

```py
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
```

## The bubble sort

The essence of this algorithm is simple: we compare the adjacent elements, and by swapping some of them, we achieve our goal.

```py
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
```
```py
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
```
ts output is [1].

This inconspicuous part of the code described as [:] is able to produce a brand new list.

```py
Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
```
A slice of this form makes a new (target) list, taking elements from the source list - the elements of the indices from start to **end - 1.**

## Copying some part of the list.
```py
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
```
[8, 6]

```py
my_list = [10, 8, 6, 4, 2]
print(my_list[:])
```
[10, 8, 6, 4, 2]

## Slices - negative indices

```py
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
```

The snippet's output is:

[8, 6, 4]

```py
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
```

This is why its output is: [10, 8, 6].

Similarly, if you omit the end in your slice, it is assumed that you want the slice to end at the element with the index len(my_list).

The previously described del instruction is able to delete more than just a list's element at once - it can delete slices too:


```py
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
```


## The in and not in operators

Python offers two very powerful operators, able to look through the list in order to check whether a specific value is stored inside the list or not.

These operators are:

```py
elem in my_list
elem not in my_list
```

```py
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5

for i in range(len(my_list)):
    if my_list[i] == to_find:  # Check if the current element matches
        print("Element found at index", i)
        break
else:
    # This block executes if the loop completes without a `break`
    print("Absent")
```

## Lists in lists

```py
row = []

for i in range(8):
    row.append(WHITE_PAWN)
 ```

The board variable is now a two-dimensional array. It's also called, by analogy to algebraic terms, a matrix.

## How functions work

```py
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
```

It's important to remember that positional arguments mustn't follow keyword arguments. That's why if you try to run the following snippet:

```py
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error
```

### return 
```py
def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print()
x = boring_function()
print("This lesson is boring...")
print(x)
```
output 

```py
This lesson is interesting!
'Boredom Mode' ON.

'Boredom Mode' ON.
This lesson is boring...
123
```
### None 
```py
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))
```

Leap year 

```py
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
```

```py
def is_year_leap(year):
    # Determines if a year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Validate inputs
    if year < 1 or month < 1 or month > 12:
        return None  # Invalid year or month

    # Days in each month for a non-leap year
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust February for leap years
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return month_lengths[month - 1]

# Test the function
test_years = [1900, 2000, 2016, 1987, 2023, 2024]
test_months = [2, 2, 1, 11, 13, 2]
test_results = [28, 29, 31, 30, None, 29]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(f"{yr}, {mo} -> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print(f"Failed (Expected: {test_results[i]}, Got: {result})")
```

**Scenario**

A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.
Complicated? Not at all. For example, 8 isn't a prime number, as you can divide it by 2 and 4 (we can't use divisors equal to 1 and 8, as the definition prohibits this).
On the other hand, 7 is a prime number, as we can't find any legal divisors for it.


Your task is to write a function checking whether a number is prime or not.

The function:

- is called is_prime;
- takes one argument (the value to check)
- returns True if the argument is a prime number, and False otherwise.

Hint: try to divide the argument by all subsequent values (starting from 2) and check the remainder - if it's zero, your number cannot be a prime; think carefully about when you should stop the process.

If you need to know the square root of any value, you can utilize the ** operator. Remember: the square root of x is the same as x0.5


Run your code and check whether your output is the same as ours.

Expected output
2 3 5 7 11 13 17 19

```py
def is_prime(num):
    # A prime number is greater than 1
    if num <= 1:
        return False
    
    # Check divisors from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# Test the function for numbers 2 through 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
```
**Scenario**

A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

The functions:

- are named liters_100km_to_miles_gallon and 
- miles_gallon_to_liters_100km respectively;
- take one argument (the value corresponding to their names)
Complete the code in the editor.

Run your code and check whether your output is the same as ours.
Here is some information to help you:

1 American mile = 1609.344 metres;

1 American gallon = 3.785411784 litres.


```py
def liters_100km_to_miles_gallon(liters):
    # 1 mile = 1609.344 meters, 1 gallon = 3.785411784 liters
    miles_per_100km = 100 * 1000 / 1609.344  # Convert 100 km to miles
    gallons = liters / 3.785411784           # Convert liters to gallons
    return miles_per_100km / gallons         # Calculate miles per gallon

def miles_gallon_to_liters_100km(miles):
    # 1 mile = 1609.344 meters, 1 gallon = 3.785411784 liters
    km_per_mile = 1609.344 / 1000           # Convert miles to kilometers
    liters_per_100km = 100 / (miles * km_per_mile) * 3.785411784
    return liters_per_100km

# Testing the functions
print(liters_100km_to_miles_gallon(3.9))  # Expected: ~60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # Expected: ~31.36194444444444
print(liters_100km_to_miles_gallon(10.0)) # Expected: ~23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # Expected: ~3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # Expected: ~7.490910297239916
print(miles_gallon_to_liters_100km(23.5)) # Expected: ~10.009131205673757
```
Look at the difference in output in the following two examples:

```py
# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
#          Happy Birthday

```
## Functions and scopes

A variable existing outside a function has a scope inside the functions' bodies.

```py
def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
```
Output 
```py
Do I know that variable? 2
1
```

There's a special Python method which can extend a variable's scope in a way which includes the functions' bodies (even if you want not only to read the values, but also to modify them).

Such an effect is caused by a keyword named global:

```py 
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
```

Output

```py
Do I know that variable? 2
2
```

The conclusion is obvious - changing the parameter's value doesn't propagate outside the function (in any case, not when the variable is a scalar, like in the example).

```py
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
```

Output
```py
I got 1
I have 2
1
```
it is different with lists 
```py
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
```

Output

```py
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [3]
Print #4: [3]
Print #5: [3]
```
When my_function(my_list_2) is called, the following happens:

The variable my_list_2 (a list [2, 3]) is passed as an argument to the parameter my_list_1.

Both my_list_1 and my_list_2 now refer to the same list object in memory. This is because lists in Python are mutable and passed by reference.


## Fibonacci numbers

They are a sequence of integer numbers built using a very simple rule:

- the first element of the sequence is equal to one (Fib1 = 1)
- the second is also equal to one (Fib2 = 1)
- every subsequent number is the the_sum of the two preceding numbers:
(Fibi = Fibi-1 + Fibi-2)

Here are some of the first Fibonacci numbers:
```py
fib_1 = 1
fib_2 = 1
fib_3 = 1 + 1 = 2
fib_4 = 1 + 2 = 3
fib_5 = 2 + 3 = 5
fib_6 = 3 + 5 = 8
fib_7 = 5 + 8 = 13
```
```py
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

```

## Recursion

recursion is a technique where a function invokes itself.

These two cases seem to be the best to illustrate the phenomenon - factorials and Fibonacci numbers. Especially the latter.

The Fibonacci numbers definition is a clear example of recursion. 

Fibi = Fibi-1 + Fibi-2

The factorial has a second, recursive side too. Look:

n! = 1 × 2 × 3 × ... × n-1 × n


It's obvious that:

1 × 2 × 3 × ... × n-1 = (n-1)!


So, finally, the result is:

n! = (n-1)! × n

This is in fact a ready recipe for our new solution.


```py
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

```
 **If you forget to consider the conditions which can stop the chain of recursive invocations, the program may enter an infinite loop.**

```py
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))
```

Recursive calls consume a lot of memory, and therefore may sometimes be inefficient.

```py
# Recursive implementation of the factorial function.

def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24

```

Ig the factorial function has no termination condition (no base case), Python will raise an exception (RecursionError: maximum recursion depth exceeded)
```py
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))
```
Outcpme 56

## What is a tuple?

You've encountered one Python sequence so far - the list. The list is a classic example of a Python sequence, although there are some other sequences worth mentioning, and we're going to present them to you now.

**Immutable data cannot be modified**

The data type we want to tell you about now is a tuple. A tuple is an immutable sequence type. It can behave like a list, but it mustn't be modified in situ.

The first and the clearest distinction between lists and tuples is the syntax used to create them - tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas.
```py
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)
```
output 

```py
(1, 2, 4, 8)
(1.0, 0.5, 0.25, 0.125)
```

f you want to create a one-element tuple, you have to take into consideration the fact that, due to syntax reasons (a tuple has to be distinguishable from an ordinary, single value), you must end the value with a comma:
```py
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
```


