from tkinter import Frame, PhotoImage, Label, Button
from functools import partial
from warnings import warn
import time

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
        current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
        self.time_label.config(text=current_time)
        self.time_label.after(200,self.tick)

    def setSubHeading(self, sub_heading):
        heading_label = Label(self, text=sub_heading, font=('orbitron', 13), fg='white', bg='#0077e6' )
        heading_label.pack()

    def createLeftSubHeading(self, sub_heading):
        heading_label = Label(self, text=sub_heading, font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        heading_label.pack(fill='x')

    def createRightSubHeading(self, sub_heading):
        heading_label = Label(self, text=sub_heading, font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        heading_label.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)

    #frame for buttons
    def createButtonFrame(self):
        self.button_frame = Frame(self,bg='#80c1ff')
        self.button_frame.pack(fill='both', expand=True)
        self.button_row = 0
        self.button_col=0

    def createPictureInFrame(self, image_path):
        image = PhotoImage (file=image_path)
        image_label = Label(self.button_frame, image=image)
        image_label.place(relx=0.6, rely=0)
        image_label.image = image

    def changePages(self, page_name):
        self.controller.show_frame(page_name)

    def getButtonFrame(self):
        # make sure button frame exists 
        try:
            self.button_frame
        except NameError:
            self.createButtonFrame()
            warn("Main button frame did not exist... Manually creating button frame")
        return self.button_frame

    # add button to main button frame - and got to new row 
    def autoAddButton(self, button_text, button_command, style='raised', 
                      borderwidth=3, width=50,height=5):
        button_frame = self.getButtonFrame()
        button = Button(button_frame, text=button_text, command=button_command,
                        relief=style,borderwidth=borderwidth, width=width,height=height)
        button.grid (row=self.button_row,column=self.button_col, pady=5)
        self.button_row+=1

    def setButtonRow(row: int):
        self.button_row = row

    def setButtonCol(col: int):
        self.button_col = col

    def createChangePageButton(self, page_name, button_text):
        change_page_func = partial(self.changePages, page_name)
        self.autoAddButton(button_text, change_page_func)
        