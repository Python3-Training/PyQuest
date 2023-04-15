#!/usr/bin/env python3
'''
KP3003: Data Detection
Create a function that can:

(1) Accept a 'tab delimited' string
(2) Return a tuple of values found
(3) Create test cases
'''

def tab_values(data:str)->():
    return ()


errors = False

print("Test: Not a string")
acase = tab_values(11)
print("Case: Should still be a tuple")
if not isinstance(acase, tuple):
    errors = True
    print("\tError.")
print("Case: Tuple should be empty")
if acase:
    errors = True
    print("\tError.")
    
print("Test: Sparse Population")
acase = tab_values('11\t\t')
print("Case: Should still be a tuple")
if not acase:
    errors = True
    print("\tError.")
print("Case: Not all columns")
if len(acase) != 3:
    errors = True
    print("\tError.")
print("Case: First was an integer")
if not isinstance(acase[0], int):
    errors = True
    print("\tError.")
    
print("Test: Proper Population")
acase = tab_values('123.45\tname\there')
print("Case: Not found")
if not acase:
    errors = True
    print("\tError.")
print("Case: Not tuple")
if not isinstance(acase, tuple):
    errors = True
    print("\tError.")
print("Case: Not all values")
if len(acase) != 3:
    errors = True
    print("\tError.")
print("Case: First was a float")
if not isinstance(acase[0], float):
    errors = True
    print("\tError.")

# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



