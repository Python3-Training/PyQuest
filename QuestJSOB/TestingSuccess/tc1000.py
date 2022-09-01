#!/usr/bin/env python3
# Mission: Time to lock this one down.

import os
import os.path
import sys
sys.path.insert(0, '.')
sys.path.insert(0, '../../')

import json
from QuestJSOB.JSOB import *
from QuestJSOB.Questions import *
from QuestJSOB.QuestExchange import EncodedJSOB as EncodedJSOB

def get_text_cases() -> list:
    template = Quest.Source()
    results = []
    results.append(Quest(template))
    datum = Quest(template)
    datum.answer = 'This\\\n \tis\t a `basic` test.'
    datum.question = datum.answer
    results.append(datum)
    return results

def get_text_file_name():
    return "./TextFile.tmp~"

def cleanup():
    fn = get_text_file_name()
    if os.path.exists(fn):
        os.unlink(fn)
    assert(os.path.exists(fn) == False)

def tc_1001():
    cleanup()
    data = get_text_cases()
    fn = get_text_file_name()
    assert(Quest.Sync(data, fn))
    data2 = Quest.Load(fn, True, True)
    assert(str(data) == str(data2))
    cleanup()
    for dat in data:
        payload = EncodedJSOB.to_share(dat)
        restored = EncodedJSOB.from_share(payload)
        assert(str(restored) == str(dat))
        assert(repr(restored) == repr(dat))
    legacy_encoded = '''
Hey, nagy - Ceck this out!
BEGIN_BLOCK$
0y123|0y39|0y73|0y68|0y39|0y58
|0y32|0y53|0y44|0y32|0y39|0y75|0y73|0y68|0y39$
0y58|0y32|0y39|0y116|0y98|0y100|0y39|0y44|0y32|
0y39|0y71|0y73|0y68|0y39|0y58
$0y32|0y39|0y57|0y49|0y65|0y54|0y48|0y52|0y51|0y65|0y45|0y48|0y56|0y50|0y48$0y45|0y49|0y49|0y69|0y66|0y45|0y57|0y56|0y57|0y66|0y45|0y67|0y52|0y51|0y52$0y54|0y66|0y48|0y55|0y66|0y48|0y68|0y50|0y39|0y44|0y32|0y39|0y100|0y105|0y102$0y102|0y105|0y99|0y117|0y108|0y116|0y121|0y39|0y58|0y32|0y39|0y101|0y120|0y112|0y101$0y114|0y116|0y39|0y44|0y32|0y39|0y97|0y115|0y115|0y111|0y99|0y105|0y97|0y116|0y105$0y111|0y110|0y39|0y58|0y32|0y39|0y95|0y83|0y81|0y76|0y39|0y44|0y32|0y39|0y115$0y116|0y97|0y116|0y117|0y115|0y39|0y58|0y32|0y39|0y103|0y116|0y103|0y39|0y44|0y32$0y39|0y113|0y117|0y101|0y115|0y116|0y105|0y111|0y110|0y39|0y58|0y32|0y39|0y87|0y104$0y97|0y116|0y32|0y105|0y115|0y32|0y116|0y104|0y101|0y32|0y100|0y105|0y102|0y102|0y101$0y114|0y101|0y110|0y99|0y101|0y32|0y98|0y101|0y116|0y119|0y101|0y101|0y110|0y32|0y68$0y77|0y76|0y44|0y32|0y97|0y110|0y100|0y32|0y68|0y81|0y76|0y32|0y105|0y110|0y32$0y83|0y81|0y76|0y63|0y39|0y44|0y32|0y39|0y97|0y110|0y115|0y119|0y101|0y114|0y39$0y58|0y32|0y39|0y92|0y92|0y611|0y615|0y83|0y116|0y97|0y110|0y100|0y97|0y114|0y100$0y32|0y83|0y81|0y76|0y32|0y99|0y111|0y109|0y109|0y97|0y110|0y100|0y32|0y99|0y97$0y116|0y101|0y103|0y111|0y114|0y105|0y101|0y115|0y58|0y92|0y92|0y611|0y615|0y68|0y68$0y76|0y32|0y68|0y97|0y116|0y97|0y32|0y68|0y101|0y102|0y105|0y110|0y105|0y116|0y105$0y111|0y110|0y32|0y76|0y97|0y110|0y103|0y117|0y97|0y103|0y101|0y92|0y92|0y611|0y615$0y68|0y81|0y108|0y32|0y68|0y97|0y116|0y97|0y32|0y81|0y117|0y101|0y114|0y121|0y32$0y76|0y97|0y110|0y103|0y117|0y97|0y103|0y101|0y92|0y92|0y611|0y615|0y68|0y77|0y76$0y32|0y68|0y97|0y116|0y97|0y32|0y77|0y97|0y110|0y105|0y112|0y117|0y108|0y97|0y116$0y105|0y111|0y110|0y32|0y76|0y97|0y110|0y103|0y117|0y97|0y103|0y101|0y92|0y92|0y611$0y615|0y68|0y67|0y76|0y32|0y68|0y97|0y116|0y97|0y32|0y67|0y111|0y110|0y116|0y114$0y111|0y108|0y32|0y76|0y97|0y110|0y103|0y117|0y97|0y103|0y101|0y92|0y92|0y611|0y615$0y39|0y125|
$END_BLOCK--Like, whoah dude - "this is \O/ might be 'kewel?!"


'''
    quest1 = EncodedJSOB.from_share(legacy_encoded)
    assert(quest1)
    quest2 = EncodedJSOB.from_share(EncodedJSOB.to_share(quest1))
    s1 = repr(quest1); s2 = repr(quest2)
    assert(s1 == s2)


if __name__ == '__main__':
    tc_1001()
    print("Testing Success.")

