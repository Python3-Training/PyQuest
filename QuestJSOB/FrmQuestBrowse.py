#!/usr/bin/env python3
#
# Author: Randall Nagy
# Mission: Browse the Quest()ions - ONLY!

import os
import sys
sys.path.insert(0, '.')
sys.path.insert(0, '../')
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
from tkinter.filedialog import askopenfilename
from collections import OrderedDict

from QuestJSOB.JSOB import *
from QuestJSOB.TkFrames import TkForm
from QuestJSOB.TkMacro import *
from QuestJSOB.Questions import Quest as Quest
from QuestJSOB.QuestExchange import EncodedJSOB
from QuestJSOB.DlgMessage import *

class FrmQuestBrowse(TkForm):
    ''' Data importation Form '''
    def __init__(self):
        super().__init__()
        self.parent = None
        self._data = list()
        self._frame = None
        self._name_tag = None
        self._text_item = None
        self._pw_quest = None
        self._pw_index = -1
        self._pw_index_found = -1
        self._lstbx_items = None
        self._sb_items = None
        self._buttons = {}
        self._dlg_find = DlgMsgCache(self.parent)

    def _show_item(self, index) -> bool:
        try:
            if index < 0:
                return
            view = self._data[index]
            block = str(view)
            McText.upl(self._text_item, block)
            McListbox.set_selected(self._lstbx_items, index)
            self.parent.show_status(f'Item ID# {view.ID}')
        except:
            return False
        return True

    def _on_browse_click(self, vevent):
        try:
            line = McListbox.get_selected(self._lstbx_items)
            if line:
                pos = line.find('\t')
                if pos == -1:
                    return
                else:
                    index = int(line[0:pos]) - 1
                    self._pw_index = index
                    self._pw_quest = self._data[index]
                    self._show_item(index)
                    self._pw_index_found = index
        except Exception as ex:
            # self.parent.show_error("Unexpected Exception", str(ex))
            pass # observed!
        finally:
            self._set_button_state()

    def _on_sel_encode(self):
        if not self._pw_quest:
            self.parent.show_error(
                "No Data", 
                "Please select an item to encode?")
            return
        encoded = EncodedJSOB.to_share(self._pw_quest)
        McText.unlock(self._text_item)
        McText.put(self._text_item, encoded)
        McText.lock(self._text_item)

    def _on_text_decode(self):
        if not McText.has_text(self._text_item):
            return
        text = McText.get(self._text_item).strip()
        if not EncodedJSOB.is_encoded(text):
            return
        self._pw_quest = None
        try:
            self._pw_quest = EncodedJSOB.from_share(text)
            if not self._pw_quest:
                self.parent.show_error(
                    "Unsuported Format", 
                    "Unknown JSOB format. Time to upgrade?")
                return
            block = str(self._pw_quest)
            McText.upl(self._text_item, block)
            self.parent.title('JSOB Question Decoded.')
            return
        except:
            self.parent.show_error(
                "Unsuported Dictionary Format", 
                "Unsuported JSOB data. Time to upgrade?")

    def _on_keep_import(self):
        if not McText.has_text(self._text_item):
            self.parent.show_error(
                "No Data", 
                "Please paste an item to import?")
            return
        self._pw_quest = None
        text = McText.get(self._text_item)
        if not EncodedJSOB.is_encoded(text):
            self.parent.show_error(
                "Encoded Data", 
                "Please paste an encoded question.")
            return
        text = EncodedJSOB.decode(text)
        quest = None
        try:
            zdict = eval(text)
            quest = Quest(zdict)
            if quest.GID != 'tbd':
                for q in self._data:
                    if quest.GID == q.GID:
                        DlgMsg.show_error(self.parent,
                            "Duplicate Global-Identifier",
                            "Unable to add this 'keep' item "
                            "to the active database; "
                            "a question with a maching GID already "
                            "exists. -Consider using another database?")
                        return
            self.parent.form_data('C', self._name_tag, quest)
        except:
            pass
        if not quest:
            self.parent.show_error(
                "Dictionary Format Error", 
                "Unsuported JSOB data. Time to upgrade?")
            return        

    def _on_clip_to_text(self):
        text = None
        try:
            text = self.parent.clipboard_get().strip()
        except:
            pass
        if not text:
            self.parent.show_error(
                "No Data", 
                "The clipboard is empty?")
            return
        self._pw_quest = None
        McText.upl(self._text_item, text)

    def _on_text_to_clip(self):
        if not McText.has_text(self._text_item):
            self.parent.show_error(
                "No Data", 
                "Please select an item to copy to the clipboard?")
            return
        if not self._pw_quest:
            self.parent.show_error(
                "No Item Selected", 
                "Please select a question to copy to the clipboard.")
            return
        encoded = McText.get(self._text_item).strip()
        if not EncodedJSOB.is_encoded(encoded):
            encoded = EncodedJSOB.to_share(self._pw_quest)
        self.parent.clipboard_clear()
        self.parent.clipboard_append(encoded)
        self.parent.title(f"Copied {self._pw_quest.ID} to Clipboard")

    def _on_locate(self):
        if self._pw_index < 0:
            return
        if self._pw_index_found < 0:
            self._pw_index_found = self._pw_index

        matcher = self._dlg_find.get_results("Find Next Item", "Item Contents:")
        if not matcher:
            return
        for which in range(self._pw_index_found + 1, len(self._data)):
            item = self._data[which]
            if item.contains(matcher):
                self._show_item(which)
                self._pw_index_found = which
                return
        for which in range(0, self._pw_index_found):
            item = self._data[which]
            if item.contains(matcher):
                self._show_item(which)
                self._pw_index_found = which
                return
        self.parent.show_status('Item not found.')

    def _on_quit(self):
        self.parent.form_done(False,self._name_tag,{})

    def destroy(self):
        if self._frame:
            self._frame.destroy()

    def _set_button_state(self):
        if self._pw_index < 0:
            for key in self._buttons:
                ref = self._buttons[key]
                ref['state'] = DISABLED
        else:
            for key in self._buttons:
                ref = self._buttons[key]
                ref['state'] = NORMAL

    def create_form(self, zframe, name_tag):
        ''' Creates another TkForm. Return TkForm / self. '''
        self.parent = zframe
        self._name_tag = name_tag

        # Parent Frame
        self._frame = PanedWindow(zframe)

        # LabelFrame Sidebar
        zlf_sidem = LabelFrame(self._frame, text=" Actions   ",
                               bg='dark green', fg='gold')

        btn = Button(zlf_sidem, text="Encode", width=10, command=self._on_sel_encode)
        btn.pack()
        self._buttons['encode'] = btn
        btn = Button(zlf_sidem, text="Decode", width=10, command=self._on_text_decode)
        btn.pack()
        self._buttons['decode'] = btn
        Label(zlf_sidem, text="", width=10).pack()
        btn = Button(zlf_sidem, text="Copy", width=10, command=self._on_text_to_clip)
        btn.pack()
        self._buttons['copy'] = btn
        btn = Button(zlf_sidem, text="Paste", width=10, command=self._on_clip_to_text)
        btn.pack()
        self._buttons['paste'] = btn
        btn = Button(zlf_sidem, text="Find", width=10, command=self._on_locate)
        btn.pack()
        self._buttons['find'] = btn
        Label(zlf_sidem, text="", width=10).pack()
        btn = Button(zlf_sidem, text="Keep", width=10, command=self._on_keep_import)
        btn.pack()
        self._buttons['keep'] = btn

        # LabelFrame Top
        zlf_items = LabelFrame(self._frame, 
                               text=" Questions  ", 
                               bg='dark green', fg='white')

        self._lstbx_items, self.sb_items = McListbox.create(zlf_items)
        McGrid.fill_cell(zlf_items, self._lstbx_items, 0, 0)
        self._lstbx_items.bind('<<ListboxSelect>>', self._on_browse_click)

        # LabelFrame Center
        zlf_item = LabelFrame(self._frame, text=" Quest  ",
                              bg='dark green', fg='white')

        self._text_item = Text(zlf_item, bg='light gray')
        McGrid.fill_cell(zlf_item, self._text_item, 0, 0)

        McText.lock(self._text_item)

        self._frame.add(zlf_sidem)
        self._frame.add(zlf_items)
        self._frame.add(zlf_item)
        zlf_sidem.grid(row=0, column=0, sticky=N+E)
        zlf_items.grid(row=0, column=1, sticky=NSEW)
        McGrid.fill_cell(self._frame, zlf_item, 1, 1) # Highlander effect?

        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)
        self._frame.pack(anchor=CENTER, fill=BOTH, expand=True)
        self._set_button_state()
        return self

    def get_data(self, quest_data) -> bool:
        ''' Return: True if the data is assigned '''
        if not isinstance(quest_data, dict):
            return False
        quest_data.clear()
        quest_data.extend(self._data)
        return True

    def put_data(self, quest_data) -> bool:
        ''' Return: True if the data is able to be used '''
        if not isinstance(quest_data, list):
            return False
        if not quest_data:
            return False
        self._data.clear()
        self._data.extend(quest_data)
        short = list()
        for ss, quest in enumerate(quest_data):
            short.append(f'{str(ss+1):>04}\t {quest.question[0:80]} ...')
        McListbox.set(self._lstbx_items, short)
        self._pw_index = self._pw_index_found = -1
        return True

