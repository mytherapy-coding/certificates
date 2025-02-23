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
print()
from platform import machine

print(machine())
print()
from platform import processor

print(processor())
print()
from platform import system

print(system())
print()
from platform import version

print(version())
print()

import platform

print(len(platform.python_version_tuple()))
print()

from random import randint
for i in range(2):
    print(randint(1, 2))
print()

for x in (el * 2 for el in range(5)):
    print(x)

print()

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print("-----?-----")
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
print()

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
print()

alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet1 = alphabet
alphabet1 = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
print(alphabet1)
print()
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))
print("_____________________")
# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
x = '[' + min(t) + ']'
print(x)
print(len(x))

t = [0, 1, 2]
print(min(t))
print()
print(
'''
string
string1
''')
y = "\n\n"
print(y)
print(len(y))
print()
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4, "*") + ']')
print('[' + 'Beta'.center(6, "*") + ']')
print()

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

print()
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print()

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

print()
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())
print()

print()

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

print()

print(",".join(["omicron", "pi", "rho"]))

print()

print("[" + " tau ".lstrip() + "]")
text = "  hello  "
print("[" + text.lstrip() + "]")
print("[" + text.rstrip() + "]")
print("[" + text.strip() + "]")
print()

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("", "?"))
print("Apple juice".replace("juice", ""))
print()

print("Hello, /n")
print("phi       chi\npsi".split())
print()
print("phi       chi psi".split())
print()
print("phi       chi\npsi")
print(" ".join(["phi", "chi", "psi"]))
print("".join("phi chi psi"))
print(" ".join(['phi', 'chi', 'psi']))
print()
def mysplit(strng):
    return strng.split()


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


print()

lst = [1, 2, 3]
print(lst.pop(1))

res = "awesome"
print(res.replace("e", "r", 1))

res = "awesome"
print(res.find("y"))

x ='\''
print(len(x))

print(ord('c')-ord('a'))
      
print(chr(ord('z')-2))

print('Mike'>'Mikey')


print()

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))
print()
class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self._venomous = False

version_2 = Python()
print(version_2._venomous)
version_2._venomous = not version_2._venomous
print(version_2._venomous)

print()

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        self.seconds += 1
        self.minutes += self.seconds//60
        self.seconds %= 60
        self.hours += self.minutes//60
        self.minutes %= 60
        self.hours %= 24
        
        
    def prev_second(self):
        self.seconds = self.seconds - 1 +60 
        self.minutes = self.minutes - (1 - self.seconds//60) +60
        self.seconds %= 60
        self.hours = self.hours - (1 - self.minutes//60) +24
        self.minutes %= 60
        self.hours %= 24
        


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

print()
class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

import sys
string_1 = "Mary had a little "
string_2 = sys.intern("Mary had a little lamb")
string_1 = sys.intern(string_1 + "lamb")

string_3 = sys.intern("Mary had a little lamb")


print(string_1 == string_2, string_1 is string_2, string_2 is string_3)
print(id(string_1), id(string_2), id(string_3))
print()


string_1 = sys.intern(string_1)

print(id(string_1), id(string_2), id(string_3))

print()

a = (1, 2, 3, 4)
b = (1, 2, 3, 4)
print(a == b)
print(a is b)
print()

import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")


print(3j)
x = 3j
y = x*x 
print(x, y)

class Fib:
    def __init__(self):
        print("__init__")
        self.i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

f = Fib()
it = iter(f)
print(it is f)
for _ in range(10):
    print(next(it))

for _, y in zip(range(10), Fib()):
    print(y)
    
print([y for _, y in zip(range(10), Fib())])

print()

print("Mike">"Mikey")

print(ord("c") - ord("a"))
print()
x = '\''
print(len(x))

print(chr(ord("z") -2))

print("My_filter")



def myfilter(f, lst):
    for x in lst:
        if f(x):
            yield x

print(list(myfilter(lambda x: x%2 == 0, [2, 4, 6, 13])))




def filter_numbers(x):
    return x == 1 or x == 5 or x == 17


print(list(filter(filter_numbers, [1, 2, 5, 9, 15])))
print()
print(list(myfilter(filter_numbers, [1, 2, 5, 9, 15])))
print()
print(list(myfilter(lambda x: x in (1,5,17), [1, 2, 5, 9, 15])))
print(list(myfilter(lambda x: x == 1 or x == 5 or x == 17, [1, 2, 5, 9, 15])))

print()

'''
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)
'''
print()
def powers_of_2():
    power = 1
    while True:
        yield power
        power *= 2

for _, v in zip(range(8), powers_of_2()):
    print(v)

print()

def powers_of_2(n):
    power = 1
    for j in range(n):
        yield power
        power *= 2

print(list(powers_of_2(20)))
for i in range(1000):
    if i in powers_of_2(20):
        print(i)
print()
powers = list(powers_of_2(20))
print(powers)
for i in range(1000):
    if i in powers:
        print(i)

print()
powers = set(powers_of_2(20))
print(powers)
for i in range(1000):
    if i in powers:
        print(i)
print(hash("117"))

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

res = [1, 3, 5, 7, 9, 10]
a = res[-2:-1]
a = res[-2:]
a = res[-2:6]

print(a)

print()

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
        print(f"f({x})={fun(x)}")


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function(range(-2, 3), poly)

print()

print_function(range(-2, 3), lambda x: 2 * x**2 - 4 * x + 2)
print()
from datetime import date

my_date = date(2019, 11, 4)
print(my_date)

print()
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print()
import calendar
print(calendar.calendar(2025))
print()

x = "\\\\"
print(len(x))

print("________")

import math
print(dir(math))

print()

