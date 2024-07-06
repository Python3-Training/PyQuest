#!/usr/bin/env python3

# Nagy's PyQuest Project Collection
# Some inspiration to assist with your solution!
# Soft9000.com

'''
KP2002: Parsing Strings
Create a function that can:

(1) Accept a 'tab delimited' string
(2) Return a tuple of strings
(3) Create test cases
'''

def split_tabs(data:str)->():
    return ()


errors = False

print("Test: Not a string")
acase = split_tabs(11)
print("Case: Should still be a tuple")
if not isinstance(acase, tuple):
    errors = True
    print("\tError.")
print("Case: Tuple should be empty")
if acase:
    errors = True
    print("\tError.")
    
print("Test: Sparse Population")
acase = split_tabs('11\t\t')
print("Case: Should still be a tuple")
if not acase:
    errors = True
    print("\tError.")
print("Case: Not all columns")
if len(acase) != 3:
    errors = True
    print("\tError.")
    
print("Test: Proper Population")
acase = split_tabs('123.45\tname\there')
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

# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



