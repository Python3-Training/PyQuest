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

    def __from_human_line(self, data) -> str:
        ''' Encode a single-line for json parsing '''
        if data.find('\r'):
            data = data.replace('\r\n', '\n')
        return self.encode(data)

    def __parse_one(self, zlines, exceptional = False) -> dict:
        try:
            result = {}
            hold = eval(' '.join(zlines))
            for key in hold:
                val = hold[key]
                if not isinstance(val, str):
                    result[key] = val
                else:
                    result[key] = self.decode(val)
            return result

        except Exception as ex:
            self.last_execption = ex
            if exceptional:
                raise ex
        return None
    
    def load_by_json(self) -> str:
        ''' Reads file, converting JSON's 'human readable' multiline escapes, to inline \\n style. '''
        self.last_execption = None
        try:
            with open(self.file, encoding='utf-8') as fh:
                return self.__from_human_line(fh.read())
        except Exception as ex:
            self.last_exception = ex
        return ''

    def load_by_eval(self, exceptional=False) -> list:
        ''' Parses one dictionary-entry, at-a-time, using eval - NOT THE JSON PARSER. '''
        self.last_execption = None
        results = []; errors = 0
        try:
            with open(self.file, encoding='utf-8') as fh:
                ignore = ('[', ']')
                zlines = list()
                buffer = ''
                for ss, line in enumerate(fh, 1):
                    if line.endswith('\\\n'):
                        buffer += line
                        continue
                    if buffer:
                        buffer += line
                        line = buffer
                        buffer = ''
                    line = line.strip()
                    if line.endswith('"'):
                        line += ',' # a common gotcha
                    line = self.__from_human_line(line)
                    if not line or line in ignore:
                        continue
                    if line[0] == "}":
                        zlines.append('}')
                        dict_ = self.__parse_one(zlines, exceptional)
                        if not dict_: 
                            errors += 1
                        else:
                            results.append(dict_)
                        zlines.clear()
                    else:
                        zlines.append(line)
        except Exception as ex:
            errors += 1
            self.last_exception = ex
            if exceptional:
                raise ex
        return errors, results

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

    def sync(self, json_string) -> bool:
        ''' Save a file, backing-up if, and as, desired. '''
        if self.backup:
            if not self.snapshot():
                raise Exception(f'Unable to backup "{self.file}"?')
        try:
            with open(self.file, 'w', encoding='utf-8') as fh:
                print(json_string, end='', file=fh)
                return True
        except Exception as ex:
            self.last_exception = ex
        return False

