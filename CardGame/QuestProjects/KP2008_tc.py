#!/usr/bin/env python3

# Nagy's PyQuest Project Collection
# Some inspiration to assist with your solution!
# Soft9000.com
# Groups:
#    https://www.facebook.com/PythonVideo/
#    https://www.facebook.com/groups/pyquest

'''
*****
KP2008: Pickling
Create a class to create, delete, update,
read, and list dated journal entries using
a "pickle" file.

(1) Use argparse to create a command-line user 
    interface (C.L.I)
(2) Include a way to delete the pickle file
(3) Create extensive test cases
'''
import time
import pickle
import os.path

class Logger:

    def load(self)->list[str]:
        '''Read & return everything in the pickle file. '''
        pass

    def create(self, line)->bool:
        '''Date-stamp & append a line to the log file. '''
        pass
        
    def read(self, which)->str:
        '''Read a ones-based entry number. '''
        pass
        
    def list(self, start:int, count:int)->list[str]:
        '''List starting with a ones-based entry number. '''
        pass
        
    def update(self, which:int, *values)->bool:
        '''Update a ones-based entry number. '''
        pass
        
    def delete(self, which:int)->bool:
        '''Delete a ones-based entry number. '''
        pass
        
    def reset(self):
        '''Remove the entire log file. '''
        pass

    @staticmethod
    def CLI(options):
        '''Manage the CLI options. '''
        pass

def test_comp(*tr):
    lines = Logger().load()
    if len(*tr) != len(lines):
        print("Error: len() mismatch.")
        return False
    for ss, line in enumerate(lines):
        left = tr[0][ss]; right = line[12:]
        if str(left) != str(right):
            print(f"Error: [{left}] <> [{right}]")
            return False
    return True

if __name__ == '__main__':
    success = 0
    errors = False
    test = Logger()
    test.reset()

    data = ["This", "is a", "Test!"]
    for line in data:
        if not test.create(line):
            errors = True
    tr = test.load()
    if not tr:
        errors = True
        
    if len(tr) != len(data):
        print(len(tr), len(data))
        errors = True

    for ss in range(len(data)):
        test.delete(1)
        data.pop(0)
        comp = test.load()
        if len(comp) != len(data):
            errors = True

    if test.load() != []:
        print(test.load(),"?")
        errors = True

    # Report
    if not errors:
        print("Testing Success")
        success += 1
    else:
        print("Error(s) detected")

    import argparse
    parser = argparse.ArgumentParser(prog='Logger')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--list",
                        nargs=2,
                        type=int,
                        help="list message @# for #")
    group.add_argument("-r", "--read",
                        nargs=1,
                        type=int,
                        help="show message")
    group.add_argument("-d", "--delete",
                        nargs=1,
                        type=int,
                        help='delete entry #')
    group2 = parser.add_argument_group()
    group2.add_argument("-u", "--update",
                        nargs=1,
                        type=int,
                        help="update log message")
    group2.add_argument("-c", "--create",
                        nargs=argparse.REMAINDER,
                        help='log a "message"')
    
    delta_cases = [
        [['-c', "We"],['We']],
        [['-c', "another"],['We', 'another']],
        [['-c', "test"],['We', 'another', 'test']],
        [['-c', "case need"],['We', 'another', 'test', 'case need']],
        [['-d', '2'],['We', 'test', 'case need']],
        [['-d', '24'],['We', 'test', 'case need']],
        [['-u', '1', '-c', "This", "is", "an", "update!"],['This is an update!', 'test', 'case need']],
    ]
    for test in delta_cases:
        aobj = parser.parse_args(test[0])
        Logger.CLI(aobj.__dict__)
        if test_comp(test[1]):
            print("Testing Success.")
            success += 1
        else:
            print("Testing Failure.")

    tr = Logger.CLI(parser.parse_args(['-l', '42', '5']).__dict__)
    if(tr == Logger().load()[-1]):
        print("Testing Success.")
        success += 1
    else:
        print("Testing Failure.")

    tr = Logger.CLI(parser.parse_args(['-l', '1', '3']).__dict__)
    lines = Logger().load()
    if(len(tr) != 3):
        raise Exception("Error: Listing Range Error")
    for ss in range(0, 3):
        if tr[ss] != lines[ss]:
            raise Exception(f"Listing: {tr[ss]} <> {lines[ss]}")
    print("Testing Success")
    success += 1

    tr = Logger.CLI(parser.parse_args(['-r', '1']).__dict__)
    if (tr[12:] == "This is an update!"):
        print("Testing Success.")
        success += 1
    else:
        print("Testing Failure.")

    tr = Logger.CLI(parser.parse_args(['-r', '42']).__dict__)
    if (not tr):
        print("Testing Success.")
        success += 1
    else:
        print("Testing Failure.")
    
    # Extended read-range testing
    test = Logger()
    test.reset()
    if os.path.exists(test.file):
        raise Exception("Error: File did not unlink.")
    for data in range(100):
        test.create(str(data))
    tr = Logger.CLI(parser.parse_args(['-l', '50', '6']).__dict__)
    lines = Logger().load()
    if len(tr) != 6:
        raise Exception("Error: Ranged list size error.")
    for ss in range(6):
        if lines[49 + ss] != tr[ss]:
            raise Exception("Nope")
    print("Testing Success")
    success += 1
    
    message = "All Testing Success!"
    if success != 13:
        message = "Error: Some test cases did not work?"
    sz = len(message)
    print('\n','*'*sz, message,'*'*sz, sep='\n')

