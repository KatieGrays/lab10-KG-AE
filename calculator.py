# https://github.com/KatieGrays/lab10-KG-AE.git
# Katie Gray & Ariella Efraim

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

# Make DivisionError
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def log(a, b):
    math.log(a, b)
# Make value error
def logarithm(a, b):
    math.log(a, b)

def exp(a, b):
    return a ** b
def square_root(a):
    try:
       return a ** 0.5
    except ValueError as e:
        print(f"Error: {e}")

def hypotenuse(a, b):
    math.hypot(a, b)

