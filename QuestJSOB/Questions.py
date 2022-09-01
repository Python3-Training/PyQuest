import sys
sys.path.insert(0, '.')
sys.path.insert(0, '../')

import json
from QuestJSOB.JSOB import *

class Quest():
    ''' Demonstrate how to use a basic JSON-serialized dictionary. '''
    
    FILE_DEFAULT = 'AllQuestions.json'
    
    def __init__(self, vals):
        ''' Assign a QUESTion dictionary for future use. '''
        super().__init__()
        self.ID         = vals['ID']
        self.GID        = vals['GID']
        self.KID        = vals['KID']
        self.difficulty = vals['difficulty']
        self.association= vals['association']
        self.status     = vals['status']
        self.question   = vals['question']
        self.answer     = vals['answer']
        Quest.normalize(self)

    def contains(self, search) -> bool:
        for key in Quest.Source():
            value = str(self.__dict__[key])
            if value.find(search) != -1:
                return True
        return False

    @staticmethod
    def normalize(quest_obj) -> None:
        newline = NewLine()
        template = Quest.Source()
        for ss, key in enumerate(template):
            value = quest_obj.__dict__[key]
            if isinstance(value, str):
                quest_obj.__dict__[key] = newline.decode(value)

    def __str__(self):
        result = "{\n"
        template = Quest.Source()
        for ss, key in enumerate(template):
            value = self.__dict__[key]
            if ss:
                result += ','
                result += '\n'
            if isinstance(value, str):
                result += f'\t"{key}": "{value}"'
            else:
                result += f'\t"{key}": {value}'
        result += "\n}"
        return result

    def __repr__(self):
        result = {}
        newline = NewLine()
        template = Quest.Source()
        for ss, key in enumerate(template):
            value = self.__dict__[key]
            if isinstance(value, str):
                result[key] = newline.encode(value)
            else:
                result[key] = value
        result = str(result)
        eval(result)
        return result

    @staticmethod
    def Load(file_name = FILE_DEFAULT, use_eval=True, exceptional=False):
        ''' Load a pre-existing file into a list of Quest()s '''
        zresults = list()
        coder = JSOB(file_name)
        if use_eval:
            errors, data = coder.load_by_eval(exceptional)
            if errors:
                raise Exception(f"eval: {errors} error(s) were found.")
            for dict_ in data:
                zresults.append(Quest(dict_))
        else:
            data = coder.load_by_json()
            for zdict in json.loads(data, encoding='utf-8'):
                zresults.append(Quest(zdict))
        return zresults
        
    @staticmethod
    def Renum(values):
        import uuid
        ''' Demonstrate how to work on a list of Quest()ions '''
        for ss, q in enumerate(values, 1):
            if q.GID == 'tbd':
                q.GID = str(uuid.uuid1()).upper()
            q.ID = ss
        return len(values)
        
    @staticmethod
    def Reorder(values, bGid=False):
        ''' Demonstrate how to work on a list of Quest()ions '''
        if bGid:
            return sorted(values, key=lambda a: a.KID + a.GID)
        return sorted(values, key=lambda a: a.status + a.association + a.difficulty)
        
    @staticmethod
    def Tally(values):
        ''' Demonstrate how to work on a list of Quest()ions '''
        results = {}
        for value in values:
            tags = value.association.split('|')
            tags.append('level.' + value.difficulty)
            tags.append('status.' + value.status)
            for tag in tags:
                if tag.find('zzend') != -1:
                    continue
                if tag in results:
                    results[tag] += 1
                else:
                    results[tag] = 1
        zresults = []
        for row in results:
            zresults.append(f'{results[row]:05}|{row}') 
        return sorted(zresults)
    
    @staticmethod
    def Sync(values, file_name = FILE_DEFAULT):
        ''' Save the data to a multi-line / human editable J.S.O.N database '''
        data = '['
        for ss, obj in enumerate(values):
            if ss:
                data += ','
            data += '\n'
            data += str(obj)
        data += '\n]\n'
        coder = JSOB(file_name)
        return coder.sync(data)
        
    @staticmethod
    def Source():
        ''' Get a data-source that can be used by the constructor '''
        return {
            'ID'            : -1,
            'KID'           : 'zKID',
            'GID'           : 'tbd',
            'difficulty'    : 'zdifficulty',
            'association'   : 'zassociation',
            'status'        : 'zstat',
            'question'      : 'zquestion',
            'answer'        : 'zanswer'
            }
