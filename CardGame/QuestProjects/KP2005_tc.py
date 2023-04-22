#!/usr/bin/env python3

# Nagy's PyQuest Project Collection
# Some inspiration to assist with your solution!
# Soft9000.com
# Groups:
#    https://www.facebook.com/PythonVideo/
#    https://www.facebook.com/groups/pyquest

'''
KP2005: Message Box
Define a function to create a message box.

(1) Input: Inset, message
(2) Output: Inset, centered message in a tuple
(3) Function should not draw on the screen
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

a_rect = mk_rect(1, 'One\ntwo\nThree')
if a_rect != ' *********\n *  One  *\n *  two  *\n * Three *\n *********\n':
    errors = True
print(a_rect)


# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



