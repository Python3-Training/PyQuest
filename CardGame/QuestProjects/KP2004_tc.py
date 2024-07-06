#!/usr/bin/env python3

# Nagy's PyQuest Project Collection
# Some inspiration to assist with your solution!
# Soft9000.com

'''
KP2004: Number Series
Create a function to create an inclusive number series.

(1) Input: Two integers
(2) Processing: 
(*)   Verify input data types
(*)   Order enumeration range (min->max)
(3) Return: Numerical interation 
      else 'None'
(4) Provide test cases
'''

def mk_range(i1:int, i2:int)->():
    return None

errors = False
acase = mk_range(5,1)
if acase != (1,2,3,4,5):
    print(f"Error: {acase}?")
    errors = True
else:
    print(f"Ok: {acase}")
acase = mk_range('a',1)
if acase:
    print(f"Error: {acase}?")
    errors = True
else:
    print(f"Ok: {acase}")

for tc in (1,2,3), (100,101,102):
    acase = mk_range(tc[0],tc[2])
    if acase != tc:
        print(f"No, {tc[0]} to {tc[2]}, not {acase}")
        errors = True
    else:
        print(f"Ok: {tc[0]} to {tc[2]} is {acase}")
        
# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



