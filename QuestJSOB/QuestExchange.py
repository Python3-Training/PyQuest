import sys
sys.path.insert(0, '.')
sys.path.insert(0, '../')

from QuestJSOB.JSOB import *
from QuestJSOB.Questions import Quest

class EncodedJSOB:
    ''' Rather than fight whitespaces (etc.) here is
    an easier way to encode, and to exchange, JSOB blocks.'''
    
    @staticmethod 
    def is_encoded(message):
        for char in '$|0y':
            if message.find(char) == -1:
                return False
        return True

    @staticmethod
    def to_share(quest_obj) -> str:
        ''' Copy-out object to the human-sharable format. '''
        if not isinstance(quest_obj, dict):
            return False
        clear = repr(quest_obj) # encode values.
        return EncodedJSOB.encode(clear)

    @staticmethod
    def from_share(block) -> dict:
        ''' Copy-in the human to_share(), to an object. '''
        decoded = ''
        for char in block:
            if char.isprintable():
                decoded += char
        data = EncodedJSOB.decode(decoded)
        try:
            return eval(data)
        except:
            pass
        return None

    @staticmethod 
    def encode(block) -> str:
        result = '\nBEGIN_BLOCK$\n'
        for ss, ch in enumerate(block,1):
            result += f'0y{ord(ch)}'
            if ss % 15 == 0:
                result += '$'
            else:
                result += '|'
        result += '\n$END_BLOCK\n'
        return result

    @staticmethod 
    def decode(jsob) -> str:
        result = ''
        rows = jsob.split('$')
        for row in rows:
            cells = row.strip().split('|')
            for cell in cells:
                if cell.startswith('0y'):
                    num = int(cell[2:])
                    result += chr(num)
        return result

