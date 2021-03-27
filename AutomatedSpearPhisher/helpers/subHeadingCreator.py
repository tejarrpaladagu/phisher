from tkinter import Frame, Label
# These helper functions create the sub headings on the screen
def setSubHeading(frame: Frame, sub_heading: str):
    heading_label = Label(frame, text=sub_heading, font=('orbitron', 13), fg='white', bg='#0077e6' )
    heading_label.pack()

def createLeftSubHeading(frame: Frame, sub_heading: str):
    heading_label = Label(frame, text=sub_heading, font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
    heading_label.pack(fill='x')

def createRightSubHeading(frame: Frame, sub_heading: str):
    heading_label = Label(frame, text=sub_heading, font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
    heading_label.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)