import sys
sys.path.insert(0, '.')
sys.path.insert(0, '../')

from tkinter import *
import textwrap

from QuestJSOB.TkMacro import *

class DlgMsgCache:
	''' Save + re-use a previous query result '''
	def __init__(self, parent):
		self.parent = parent
		self._last_find = ' '

	def clear(self):
		''' clear the last find '''
		self._last_find = ' '

	def get(self):
		''' get the last find '''
		return self._last_find

	def get_results(self, title : str, message : str):
		title = str(title)
		results = simpledialog.askstring(
			title, message,
			parent=self.parent,
			initialvalue=self._last_find)
		if results:
			self._last_find = results
		return results


class DlgMsg:
	''' A color-coded, parent-bethemed, set modal dialogs. '''

	@staticmethod
	def show_error(parent, title, message, msg_width=40, wrap=True):
		''' Show a dialog with a red (error) theme '''
		parent.bell()
		DlgMsg.show_message(parent, title, message, msg_width, wrap, color='red')

	@staticmethod
	def show_info(parent, title, message, msg_width=40, wrap=True, color='blue'):
		''' Show a dialog with a blue (info) theme '''
		DlgMsg.show_message(parent, title, message, msg_width, wrap, color='blue')

	@staticmethod
	def show_message(parent, title, message, msg_width=40, wrap=True, color=None):
		''' Show a dialog with the default theme '''
		dlg = None; frame=None
		try:
			loc = {
				'x': parent.winfo_x(),
				'y': parent.winfo_y(),
				'wide': parent.winfo_width(),
				'high': parent.winfo_height()
				}
			xpos = loc['x'] + (loc['wide']//4)
			ypos = loc['y'] + (loc['high']//4)

			if color:
				dlg = Toplevel(master=parent, bg=color)
				frame = Frame(dlg, bg=color)
			else:
				dlg = Toplevel(master=parent)
				frame = Frame(dlg)
			dlg.geometry(f"+{xpos}+{ypos}")
			dlg.title(title)
			dlg.resizable(False, False)
			if wrap:
				lines = textwrap.wrap(message, width=msg_width)
			else:
				lines = message
			if len(lines) > 10:
				lbox = Listbox(frame, width=msg_width + 2, height=10)
				lbox.insert(0, *lines)
				lbox.pack()
			else:
				text = Text(frame, width=msg_width + 2, height=len(lines)+2)
				McText.put(text, "\n".join(lines))
				McText.lock(text)
				text['state'] = DISABLED
				text.pack()
			Button(frame, text="Okay", command=dlg.destroy).pack()
			frame.pack()
			dlg.focus()
			dlg.grab_set() # modal
			parent.wait_window(dlg)
		finally:
			if dlg:
				dlg.destroy()





