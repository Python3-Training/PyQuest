import json

class NewLine:
    ''' Set problematic characters to unlikely ordinals whilst parsing '''
    en = {
        '\r': chr(612),
        '\n': chr(611),
        '\t': chr(615),
        r'\r': chr(616),
        r'\n': chr(617),
        r'\t': chr(618),
        r'\\n': chr(619),
        }
    
    def __init__(self):
        self.de = {}
        for key in NewLine.en:
            self.de[NewLine.en[key]] = key

    def decode(self, text) ->str:
        results = ''
        for ch in text:
            if ch in self.de:
                results += self.de[ch]
            else:
                results += ch
        return results

    def encode(self, text) ->str:
        results = ''
        for ch in text:
            if ch in NewLine.en:
                results += NewLine.en[ch]
            else:
                results += ch
        return results

class JSOB(NewLine):
    ''' A quick-fix to enable multi-line strings for Python in J.S.O.N '''
    def __init__(self, file_name, backup=True):
        super().__init__()
        self.file = file_name
        self.backup = backup
        self.last_snap = None
        self.last_execption = None
    
    def load(self) -> list:
        ''' Reads file, converting JSON's 'human readable' multiline escapes, to inline \\n style. '''
        self.last_execption = None
        try:
            with open(self.file, encoding='utf-8') as fh:
                return eval(fh.read())
        except Exception as ex:
            self.last_exception = ex
        return ''

    def snapshot(self) -> bool:
        ''' Backup the constructed file to a 'probably unique' file name. '''
        import os.path; import time; import shutil
        self.last_snap = self.file + '.' + str(time.time()) + ".tmp~"
        try:
            if not os.path.exists(self.file):
                return True
            shutil.copyfile(self.file, self.last_snap)
        except Exception as ex:
            self.last_execption = ex
            return False
        self.last_execption = None
        return True

    def sync_rows(self, rows:dict) -> bool:
        from pprint import pprint as pprint
        ''' Save a file, backing-up if, and as, desired. '''
        if self.backup:
            if not self.snapshot():
                raise Exception(f'Unable to backup "{self.file}"?')
        try:
            with open(self.file, 'w', encoding='utf-8') as fh:
                print("[\n", file=fh)
                for ss, row in enumerate(rows):
                    if ss:
                        print(",\n", file=fh)
                    pprint(row, stream=fh)
                print("\n]", file=fh)
                return True
        except Exception as ex:
            self.last_exception = ex
        return False

