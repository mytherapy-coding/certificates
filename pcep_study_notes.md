
The string is **<span style="color: red;">delimited</span>** with quotes - in fact, the quotes make the string - they cut out a part of the code and assign a different meaning to it.

**<span style="color: red;">invoke</span>** typically means to call or execute a function



### Integers: octal and hexadecimal numbers

* In Python, numbers prefixed with 0o (zero followed by a lowercase "o") are interpreted as octal numbers (base 8).
* Octal numbers use digits 0-7.

The number 123 is interpreted as an <span style="color: red;">octal number</span> due to the 0o prefix.
To convert it to decimal (base 10), you expand it as follows:

123 (octal) = 1 × 8^2 + 2 × 8^1 + 3 × 8^0
            = 1 × 64 + 2 × 8 + 3 × 1
            = 64 + 16 + 3
            = 83 (decimal)