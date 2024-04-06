#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

import math

a = int(input("What is your a value"))
b = int(input("What is your b value"))
c = int(input("what is your c value"))

x = (c-b)/a
print(f"The solution of the equationn is {x}")
