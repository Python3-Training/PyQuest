#!/usr/bin/env python3
'''
KP2003: Factorials
Create a function to show a factorial:

(1) Input: Single Integer
(2) Input: Test for non-integers
(3) Return: Success - True, Factorial
(4) Return: Error   - False, -1
(5) Provide adequate test cases
'''

def mk_fact(data:int)->():
    return False, -1

errors = False

for tc in (1,1,True), (2,2,True),\
    (3,6,True), (4,24,True),\
    (6,720,True), ('a',-1,False):
    acase = mk_fact(tc[0])
    if acase[0] != tc[2]:
        print(f"No, {tc[1]}! is not {acase[0]}")
        errors = True
    if acase[1] != tc[1]:
        print(f"No, {tc[0]}! is {tc[1]}, not {acase[1]}")
        errors = True
    else:
        print(f"Ok: {tc[0]}! is {acase}")
        
# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



