## Importing a module

```py
import math  # Importing the math module

# Defining a custom sin function
def sin(x):
    if 2 * x == pi:
        return 0.99999999  # Custom approximation of sin(pi/2)
    else:
        return None  # Returns None for other values

# Defining a custom pi variable
pi = 3.14

# Calling the custom sin function with custom pi
print(sin(pi / 2))  

# Calling the actual math.sin function with math.pi
print(math.sin(math.pi / 2))  

```
The function returns an alphabetically sorted list containing all entities' names available in the module identified by a name passed to the function as an argument:
```py
import math

for name in dir(math):
    print(name, end="\t")
```

output 

```py
__doc__	__loader__	__name__	__package__	__spec__	acos	acosh	asin	asinh	atan	atan2	atanh	ceil	copysign	cos	cosh	degrees	e	erf	erfc	exp	expm1	fabs	factorial	floor	fmod	frexp	fsum	gamma	hypot	isfinite	isinf	isnan	ldexp	lgamma	log	log10	log1p	log2	modf	pi	pow	radians	sin	sinh	sqrt	tan	tanh	trunc	
```
```py
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

```

```py
4
[3, 1, 8, 9, 10]
[10, 8, 5, 1, 6, 4, 3, 9, 7, 2]
```
## Lambdas and the map() function

```py
In the simplest of all possible cases, the map() function:

map(function, list)


takes two arguments:

- a function;
- a list.
The above description is extremely simplified, as:

the second map() argument may be any entity that can be iterated (e.g., a tuple, or just a generator)
map() can accept more than two arguments.
```
The map() function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent function results.

## Operations on strings: ord()
If you want to know a specific character's ASCII/UNICODE code point value, you can use a function named ord() (as in ordinal).

```py
# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
```
output 
```py
97
32
```
## Operations on strings: chr()

If you know the code point (number) and want to get the corresponding character, you can use a function named **chr().**

The function takes a code point and returns its character.

Invoking it with an invalid argument (e.g., a negative or invalid code point) causes ValueError or TypeError exceptions.

```py
# Demonstrating the chr() function.

print(chr(97))
print(chr(945))
```
output
```py
a
α
```

## Operations on strings: min()
```py
print(min("aAbByYzZ"))
```
output 
```py
A
```

The length of a string is determined by the len() function. The escape character (\) is not counted. For example:
```py
print(len("\n\n"))
```
outputs 2
## The capitalize() method

The capitalize() method does exactly what it says - it creates a new string filled with characters taken from the source string, but it tries to modify them in the following way:

if the first character inside the string is a letter (note: the first character is an element with an index equal to 0, not just the first visible character), it will be converted to upper-case;
all remaining letters from the string will be converted to lower-case.

```py
# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
```
output
```py
Abcd
```
## The center() method

The one-parameter variant of the center() method makes a copy of the original string, trying to center it inside a field of a specified width.

The centering is actually done by adding some spaces before and after the string.

Don't expect this method to demonstrate any sophisticated skills. It's rather simple.

The example in the editor uses brackets to clearly show you where the centered string actually begins and terminates.

```py
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
```
output

```py
[Beta]
[Beta]
[ Beta ]
```

he two-parameter variant of center() makes use of the character from the second argument, instead of a space. Analyze the example below:
```py
print('[' + 'gamma'.center(20, '*') + ']')
```

This is why the output now looks like this:
```py
[*******gamma********]
```

- If width ≤ length of the string → No padding, returns the original string.
- If width > length → Spaces are added equally on both sides.
- If width - length is odd, the extra space goes to the right.

## The endswith() method

The endswith() method checks if the given string ends with the specified argument and returns True or False, depending on the check result.

Note: the substring must adhere to the string's last character - it cannot just be located somewhere near the end of the string.

```py
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

```
output 

```py
True
False
False
True
```

## The find() method
The find() method is similar to index(), which you already know - it looks for a substring and returns the index of first occurrence of this substring, but:

it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
it works with strings only - don't try to apply it to any other sequence.

Note: don't use find() if you only want to check if a single character occurs within a string - the in operator will be significantly faster.

```py
# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))
```
output
```py
1
-1
```

