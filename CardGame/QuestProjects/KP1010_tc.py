#!/usr/bin/env python3

# Nagy's PyQuest Project Collection
# Some inspiration to assist with your solution!
# Soft9000.com

'''
*****
KP1010: Easy Logger
Create a class to append and read the lines for a file.

(1) File editable by text editors
(2) Manage exceptions
(3) Include a way to delete the file
(4) Provide a test case
'''

import os.path

class Logger:

    def __init__(self, afile:str='mylog.txt'):
        pass

    def write(self, line:str)->bool:
        pass
        
    def read(self)->[]:
        pass
    
    def reset(self):
        pass


errors = False
test = Logger()
test.reset()

data = "This", "is a", "Test!"
for line in data:
    if not test.write(line):
        errors = True
results = test.read()
if results != ["This\n", "is a\n", "Test!\n"]:
    print(results)
    errors = True

# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



