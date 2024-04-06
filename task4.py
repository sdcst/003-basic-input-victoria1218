#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math

h = int(input("What is the height of the cone?"))
r = int(input("What is the radius of the cone?"))

sa = math.pi * r*(r +(r**2+ h**2)**0.5)
print(f"The surface area of the cone is {sa}")
