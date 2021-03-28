from tkinter import Frame, PhotoImage, Label, Entry
from warnings import warn
from time import strftime

# Common Frame with header and footer
class CommonFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='#0077e6')
        self.createHeading()
        self.createFooter()
        self.tick ()

    #common heading
    def createHeading(self):
        heading_label = Label(self, text='Spear Phishing Tool', font=('orbitron', 45,'bold'), fg='white', bg='#0077e6')
        heading_label.pack(pady=25)

    def createFooter(self):
        #bottom frame for time and python logo
        bottom_frame = Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        #python develop sentence
        python_dev_label = Label(bottom_frame, text='Developed with: ', font=('orbitron', 12,'bold'))
        python_dev_label.place(relx=0)

        #python symbol
        python_image = PhotoImage (file='images/python.png')
        python_label = Label(bottom_frame, image=python_image)
        python_label.place(relx=0.11)
        python_label.image = python_image

        self.time_label = Label(bottom_frame,font=('orbitron-Bold',12))
        self.time_label.pack (side='right')
        

    #time bar at the bottom
    def tick(self):
        current_time = strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
        self.time_label.config(text=current_time)
        self.time_label.after(200,self.tick)

    #frame for buttons
    def createButtonFrame(self):
        self.button_frame = Frame(self,bg='#80c1ff')
        self.button_frame.pack(fill='both', expand=True)

    # make sure button frame exists 
    def getButtonFrame(self):
        try:
            self.button_frame
        except NameError:
            self.createButtonFrame()
            warn('WARNING: Main button frame did not exist... Manually creating button frame')
        return self.button_frame

    def setUpLabelGrid(self, start_row: int, start_col: int):
        self.label_row = start_row
        self.label_col = start_col

    def autoAddLabel(self, text: str):
        button_frame = self.getButtonFrame()
        label = Label(button_frame, text=text, font=('orbitron', 15), 
            fg='white', bg='#80c1ff',anchor='w' )
        label.grid (row=self.label_row,column=self.label_col,pady=5, ipady=20)
        self.label_row += 1

    def setUpEntryGrid(self, start_row: int, start_col: int):
        self.entry_row = start_row
        self.entry_col = start_col
        self.entry_dict = dict()

    def checkForEntryInitialization(self):
        try:
            self.entry_dict
        except NameError:
            self.setUpEntryGrid(0, 0)
            warn('WARNING: Entry field was not initialized... initializing row to 0 and column to 0')
        return self.entry_dict

    # create dictionary and get 
    def autoAddEntry(self, entry_label):
        button_frame = self.getButtonFrame()
        self.checkForEntryInitialization()
        entry = Entry(button_frame, width=59)
        entry.grid (row=self.entry_row,column=self.entry_col,pady=5, ipady=20)
        self.entry_row += 1
        self.entry_dict[entry_label] = entry

    def addLabelWithEntry(self, text: str, entry_label: str):
        self.autoAddLabel(text)
        self.autoAddEntry(entry_label)

    def getValueOfEntry(self, entry_label: str):
        self.checkForEntryInitialization()
        if entry_label in self.entry_dict:
            return self.entry_dict[entry_label].get()
        warn(f'WARNING: value "{entry_label}" does not exist')
        return ''