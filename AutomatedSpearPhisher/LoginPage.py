from tkinter import PhotoImage, Label, StringVar, Button, Entry
from config import program_password
import bcrypt
from CommonFrame import CommonFrame
#------------------------------------------Login-------------------------------------------------------
# This page shows the initial login screen 
class LoginPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        self.setWindowsAttribute()
        self.createPasswordEntry()
        self.createSubmitButton()
        self.createInvalidPasswordLabel()

    # change the title in the window and add an icon
    def setWindowsAttribute(self):
        self.controller.title ("Spear Phishing Tool")
        self.controller.state ('normal')
        self.controller.iconphoto (False, PhotoImage (file='images/scraper.png'))

    #password entry that stores password
    def createPasswordEntry(self):
        space_label = Label(self,height=4, bg='#0077e6')
        space_label.pack()

        password_label=Label(self,text='Enter password', font=('orbitron', 13), bg='#0077e6', fg='white')
        password_label.pack(pady=10)

        self.my_password = StringVar()
        password_entry_box = Entry(self, show="*", textvariable=self.my_password,font=('orbitron', 12), width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

    def createSubmitButton(self):
        enter_button = Button(self, text='Enter', command=self.check_password, relief='raised', borderwidth=3, width=40, height=3 )
        enter_button.pack(pady=10)

    def createInvalidPasswordLabel(self):
        self.incorrect_password_label = Label (self,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        self.incorrect_password_label.pack(fill='both', expand=True)

    #password enter button and checks to see if it matches password from the configuration file
    def check_password(self):
        if bcrypt.checkpw(self.my_password.get().encode('utf-8'), program_password.encode('utf-8')):
            self.my_password.set('')
            self.incorrect_password_label['text']=''
            self.controller.show_frame('MenuPage')
        else:
            self.incorrect_password_label['text']='Incorrect Password'

    