# https://github.com/KatieGrays/lab10-KG-AE.git
# Partner 1: Katie Gray 
# Partner 2: Ariella Efraim

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

# Make DivisionError
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def log(a, b):
    return math.log(a, b)

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm arguments must be positive")
    return math.log(a, b)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return None
    return a ** 0.5

def hypotenuse(a, b):
    return math.hypot(a, b)
