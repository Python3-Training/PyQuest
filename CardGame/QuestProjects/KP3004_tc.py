#!/usr/bin/env python3
'''
KP3004: Message Box
Define a class to create message boxes.

(1) Constructor: 
    (*) Box inset and default character
    (*) Default inset is 10
    (*) Default character is '*'
(2) Input: Message to display
(3) Output: Inset, centered message
    in a tuple
(4) Class will not draw the screen
(5) Create a test case
'''
class MkRect:
    pass


errors = False
a_class = MkRect()
a_rect = a_class.add_rect('This Message\nis a\nBetter TEST')
z_rect = ('          ****************\n',
          '          * This Message *\n',
          '          *     is a     *\n',
          '          * Better TEST  *\n',
          '          ****************\n')
if a_rect != z_rect:
    errors = True

a_rect = a_class.add_rect(2)

if a_rect != ('          *****\n',
              '          * 2 *\n',
              '          *****\n'):
    errors = True



# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



