#!/usr/bin/env python3
'''
KP3005: Message Boxes
Design a class to create message boxes.

(1) msg_box(x, y, msg, box='*')
(2) Message may be multi-line
(3) get_screen()->[]
(4) Create multi-message test cases
(5) Verify multiline messages
(6) Verify overlapped messages
(7) Screen size is absolute
'''
class MsgScreen:

    def __init__(self, screen_width=80, screen_height=25):
        pass
       
    def msg_box(self, x:int, y:int, message:str, box='*')->bool:
        pass

    def get_screen(self)->[]:
        pass

def dump(scr):
    '''You might need this?'''
    print()
    for ss, line in enumerate(scr, 1):
        print(ss, '[',line,']', len(line))

errors = False
area = MsgScreen(20, 8)
if not area.msg_box(2, 2, "This isa\ntest\n'thang"):
    errors = True
sol = ["                    ",
       "                    ",
       "  ************      ",
       "  * This isa *      ",
       "  *   test   *      ",
       "  *  'thang  *      ",
       "  ************      ",
       "                    "]
scr = area.get_screen()
#dump(scr)
if scr != sol:
    errors = True
if not area.msg_box(1, 1, "Pop\nUp\nWindow", '#'):
    errors = True
sol = ["                    ",
       " ##########         ",
       " #  Pop   #***      ",
       " #   Up   #a *      ",
       " # Window #  *      ",
       " ##########  *      ",
       "  ************      ",
       "                    "]
scr = area.get_screen()
if scr != sol:
    errors = True

# Report
if not errors:
    print("Testing Success")
else:
    print("Error(s) detected")



