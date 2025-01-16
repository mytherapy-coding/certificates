
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
