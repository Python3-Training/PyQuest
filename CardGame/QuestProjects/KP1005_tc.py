#!/usr/bin/env python3
'''
KP1005: Rectangles
Create a testable function that creates textual rectangles.

(1) Input: Rectangle inset, length & height
(2) Output: Inset text-rectangle in a 
    string buffer
(3) Function should not draw the rectangle 
    on the screen
(4) Create a test case
'''

def mk_rect(inset:int, width:int, height:int)->str:
    pass


errors = False
a_rect = mk_rect(1, 2, 3)
if a_rect != ' **\n **\n **\n':
    errors = True
a_rect = mk_rect('1', 2, 3)
if a_rect:
    errors = True

# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



