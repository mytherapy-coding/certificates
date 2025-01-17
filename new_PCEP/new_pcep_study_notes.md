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