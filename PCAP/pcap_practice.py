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

