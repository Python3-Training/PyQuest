#!/usr/bin/env python3
'''
KP2005: Message Box
Define a function to create a message box.

(1) Input: Inset, message
(2) Output: Inset, centered message in a tuple
(3) Function should not draw the rectangle 
    on the screen
(4) Create a test case
'''

def mk_rect(inset:int, message:str)->str:
    return ''


errors = False
a_rect = mk_rect(1, '2')
print(a_rect)

if a_rect != ' *****\n * 2 *\n *****\n':
    errors = True
a_rect = mk_rect('1', 2)
if a_rect:
    errors = True


# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



