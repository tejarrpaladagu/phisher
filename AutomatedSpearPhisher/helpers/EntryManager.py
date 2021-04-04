from tkinter import Frame, Label, Entry, END
from warnings import warn

# Entry manager creates text fields with labels 
class EntryManager:
    def __init__(self, button_frame: Frame, start_row: int, label_col: int, entry_col: int):
        if button_frame==None:
            raise ValueError
        self.button_frame = button_frame
        self.label_row = start_row
        self.entry_row = start_row
        self.label_col = label_col
        self.entry_col = entry_col
        self.entry_dict = dict()

    def autoAddLabel(self, text: str, sticky=''):
        button_frame = self.button_frame
        label = Label(button_frame, text=text, font=('orbitron', 15), 
            fg='white', bg='#80c1ff',anchor='w' )
        label.grid (row=self.label_row,column=self.label_col,pady=5, ipady=20, sticky=sticky)
        self.label_row += 1

    # create dictionary and get 
    def autoAddEntry(self, entry_label, sticky='', show='', width=59, vcmd={}, validate="none"):
        button_frame = self.button_frame
        entry = Entry(button_frame, width=width, show=show, validate=validate, validatecommand=vcmd)
        entry.grid (row=self.entry_row,column=self.entry_col,pady=5, ipady=20, sticky=sticky)
        self.entry_row += 1
        self.entry_dict[entry_label] = entry

    def addLabelWithEntry(self, text: str, entry_label: str,sticky_label='', sticky_entry='', show='', vcmd={}, validate="none"):
        self.autoAddLabel(text, sticky_label)
        self.autoAddEntry(entry_label, sticky_entry, show, vcmd=vcmd, validate=validate)

    def getValueOfEntry(self, entry_label: str):
        if entry_label in self.entry_dict:
            return self.entry_dict[entry_label].get()
        warn(f'WARNING: value "{entry_label}" does not exist')
        return ''
    
    def setValueOfEntry(self, entry_label: str, value: str):
        if entry_label in self.entry_dict:
            e=self.entry_dict[entry_label]
            e.delete(0,END)
            e.insert(0,value)
        else:
            warn(f'WARNING: value "{entry_label}" does not exist')

    def register(self, callback):
        return (self.button_frame.register(callback))