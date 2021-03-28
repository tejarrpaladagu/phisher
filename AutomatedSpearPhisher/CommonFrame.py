from tkinter import Frame, PhotoImage, Label
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

    def changePages(self, page_name: str):
        self.controller.show_frame(page_name)