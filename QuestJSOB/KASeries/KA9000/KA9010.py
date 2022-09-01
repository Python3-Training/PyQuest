#!/usr/bin/env python3
# Mission: Demonstrate how to check if instances are the same.
# File: KA9010.py

class CopyDum():
    def __init__(self, obj, check=None):
        self.obj = str(obj)
        self.check = check

    def comp(self, obj):
        if not self.check:
            print("Using id()", end=':\t')
            return id(self.obj) == id(obj)
        elif self.check is 1:
            print("Using ==", end=':\t')
            return self.obj == obj
        else:
            print("Using `is`", end=':\t')
            return self.obj is obj

my_obj = "Checker"
instances = CopyDum(my_obj), \
            CopyDum(my_obj, 1), \
            CopyDum(my_obj, 2)

print('\nManaged:')
for inst in instances:
    print(inst.comp(my_obj))

forced = str(b"Checker")
print('\nForced Copy:')
for inst in instances:
    print(inst.comp(forced))

print()
print("is:", instances[0] is instances[1])
print("==:", instances[0] == instances[1])
print("id:", id(instances[0]) == id(instances[1]))

if False: # True:
    print()
    for oper in "==", id, "is":
        print('~'*20)
        help(oper)



