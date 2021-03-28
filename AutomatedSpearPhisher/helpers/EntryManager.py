from tkinter import Frame, Label, Entry
from warnings import warn

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

    def autoAddLabel(self, text: str):
        button_frame = self.button_frame
        label = Label(button_frame, text=text, font=('orbitron', 15), 
            fg='white', bg='#80c1ff',anchor='w' )
        label.grid (row=self.label_row,column=self.label_col,pady=5, ipady=20)
        self.label_row += 1

    # create dictionary and get 
    def autoAddEntry(self, entry_label):
        button_frame = self.button_frame
        entry = Entry(button_frame, width=59)
        entry.grid (row=self.entry_row,column=self.entry_col,pady=5, ipady=20)
        self.entry_row += 1
        self.entry_dict[entry_label] = entry

    def addLabelWithEntry(self, text: str, entry_label: str):
        self.autoAddLabel(text)
        self.autoAddEntry(entry_label)

    def getValueOfEntry(self, entry_label: str):
        if entry_label in self.entry_dict:
            return self.entry_dict[entry_label].get()
        warn(f'WARNING: value "{entry_label}" does not exist')
        return ''