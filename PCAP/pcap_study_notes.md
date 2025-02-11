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

## The isalnum() method

The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.

Look at the example in the editor and run it.

Note: any string element that is not a digit or a letter causes the method to return False. An empty string does, too.

```py
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
```
output
```py
True
True
True
False
False
False
```
## The isalpha() and isdigit() method method

The isalpha() method is more specialized - it's interested in letters only.

```py
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())
```
output 
```py
True
False
```

## Demonstrating the isdigit() method:
```py
print('2018'.isdigit())
print("Year2019".isdigit())
```
output 

```py
True
False
```

## The islower() method

The islower() method is a fussy variant of isalpha() – it accepts lower-case letters only.

```py
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())
```
output 

```py
False
True
```
## The isspace() method

The isspace() method identifies whitespaces **only** – it disregards any other character (the result is False then).

```py
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
```
output

```py
True
True
False
```
## The isupper() method

The isupper() method is the upper-case version of islower() – it concentrates on upper-case letters only.

```py
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
```
output 
```py
False
False
True
```

## The join() method

The join() method is rather complicated, so let us guide you step by step thorough it:

- as its name suggests, the method performs a join - it expects one argument as a list; 
- it must be assured that all the list's elements are strings - the method will raise a TypeError exception otherwise;
- all the list's elements will be joined into one string but...
- ...the string from which the method has been invoked is used as a separator, put among the strings;
- the newly created string is returned as a result.

Take a look at the example in the editor. Let's analyze it:

- the join() method is invoked from within a string containing a comma (the string can be arbitrarily long, or it can be empty)
- the join's argument is **a list** containing three strings;
- the method returns **a new string**.

```py
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))
``` 
output 

```py
omicron,pi,rho
```

## The lower() method

The lower() method makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts, and returns the string as the result. Again, the source string remains untouched.

If the string doesn't contain any upper-case characters, the method returns the original string.

**Note: The lower() method doesn't take any parameters.**

```py
# Demonstrating the lower() method:
print("SiGmA=60".lower())
```
output

```py
sigma=60
```

## .lstrip(), .rstrip(), and .strip()

- Use .lstrip() when you want to remove spaces only from the beginning.
- Use .rstrip() when you want to remove spaces only from the end.
- Use .strip() when you want to remove spaces from both sides.
```py
text = "  hello  "
print("[" + text.lstrip() + "]")
print("[" + text.rstrip() + "]")
print("[" + text.strip() + "]")
```
output

```py
[hello  ]
[  hello]
[hello]
```
## The replace() method
The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.

Look at the example code in the editor. Run it.
```py
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
```
output

```py
www.pythoninstitute.org
Thare are it!
Apple
```

## The find() method
The find() method is similar to index(), which you already know - it looks for a substring and returns the index of **first** occurrence of this substring, but:

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
## The rfind() method
- rfind() searches for the last occurrence of a substring.
- If found, it returns the index of the last occurrence.
- If not found, it returns -1.
- You can specify a start and end range for searching.

```py text = "hello world, welcome to the world"
index = text.rfind("world", 0, 20)  
print(index)  # Output: 6
```
- Here, rfind("world", 0, 20) searches only from index 0 to 19.
- The last occurrence of "world" within this range is at index 6.

## The split() method
The split() method does what it says - it splits the string and builds a list of all detected substrings.

The method assumes that the substrings are delimited by whitespaces - the spaces don't take part in the operation, and aren't copied into the resulting list.

If the string is empty, the resulting list is empty too.
```py
# Demonstrating the split() method:
print("phi       chi\npsi".split())
```
output
```py
['phi', 'chi', 'psi']
```
## The swapcase() method

The swapcase() method makes a new string by swapping the case of all letters within the source string: lower-case characters become upper-case, and vice versa.

All other characters remain untouched.

Look at the first example in the editor. Can you guess the output? It won't look good, but you must see it:

```py
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())
```
output
```py
i KNOW THAT i KNOW NOTHING.
```

## The title() method

The title() method performs a somewhat similar function - it changes every word's first letter to upper-case, turning all other ones to lower-case.

Look at the second example in the editor. Can you guess its output? This is the result:

```py

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())
```
output
```py
I Know That I Know Nothing. Part 1.
```
## Some of the methods offered by strings are:

| Method        | Description |
|--------------|------------|
| **`capitalize()`** | Changes the first letter of the string to uppercase. |
| **`center(width)`** | Centers the string inside a field of a given width. |
| **`count(substring)`** | Counts the occurrences of a given substring in the string. |
| **`join(iterable)`** | Joins all items of a tuple/list into one string, using the string as a separator. |
| **`lower()`** | Converts all the string's letters to lowercase. |
| **`lstrip()`** | Removes white spaces from the beginning of the string. |
| **`replace(old, new)`** | Replaces a given substring (`old`) with another (`new`). |
| **`rfind(substring)`** | Finds the last occurrence of a substring in the string. |
| **`rstrip()`** | Removes trailing white spaces from the end of the string. |
| **`split(delimiter)`** | Splits the string into a list of substrings using the given delimiter. |
| **`strip()`** | Removes both leading and trailing white spaces. |
| **`swapcase()`** | Swaps uppercase letters to lowercase and vice versa. |
| **`title()`** | Converts the first letter of each word to uppercase. |
| **`upper()`** | Converts all the string's letters to uppercase. |


**String content can be determined using the following methods (all of them return Boolean values):**


| Method            | Description |
|------------------|-------------|
| **`endswith(substring)`** | Checks if the string ends with a given substring. |
| **`isalnum()`** | Checks if the string consists only of letters and digits (no special characters or spaces). |
| **`isalpha()`** | Checks if the string consists only of letters (no digits or special characters). |
| **`islower()`** | Checks if the string consists only of lowercase letters. |
| **`isspace()`** | Checks if the string consists only of whitespace characters (spaces, tabs, newlines). |
| **`isupper()`** | Checks if the string consists only of uppercase letters. |
| **`startswith(substring)`** | Checks if the string begins with a given substring. |

## Sorting

`sorted()`

The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements.

```py
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
```
output 

```py
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']
```

> The second method affects the list itself - no new list is created. Ordering is performed in situ by the method named `sort()`.

```py
# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
```
output

```py
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']
```
- > string == number is always False;
- > string != number is always True;
- > string >= number always raises an exception.

## How Python Compares Strings
Python compares strings character by character using their ASCII/Unicode values.
_____
- Lowercase letters (a-z) have higher ASCII values than uppercase letters (A-Z).
- Numbers (0-9) have lower ASCII values than letters.
- If one string is longer but identical up to the shorter string's length, the longer string is considered greater.
____

## The stack - the object approach

When any class component has a name starting with two underscores (__), it becomes private - this means that it can be accessed only from within the class.

You cannot see it from the outside world. This is how Python implements the encapsulation concept.

```py
class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()
print(len(stack_object.__stack_list))
```
Run the program to test our assumptions - an AttributeError exception should be raised.
```py
AttributeError: 'Stack' object has no attribute '__stack_list'
```

## Inheritance: issubclass()
Python offers a function which is able to identify a relationship between two classes, and although its diagnosis isn't complex, it can check if a particular class is a subclass of any other class.

This is how it looks:

```py
issubclass(ClassOne, ClassTwo)
```


The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise.