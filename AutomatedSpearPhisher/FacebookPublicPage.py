from tkinter import Label, Button, Entry
from CommonFrame import CommonFrame
# TODO: add face book public scraper
# TODO: make sure posting works on public scraper as well 
from FacebookPost import post

class FacebookPublicPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)

        #subheadings
        self.setSubHeading('Public Facebook')
        #Facebook selection path
        self.createLeftSubHeading('Please enter fields')
        self.createRightSubHeading('Previous Page: Facebook')

        #frame for buttons
        self.createButtonFrame()
        button_frame = self.getButtonFrame()

        #Facebook symbol
        self.createPictureInFrame('images/facebook.png')
        #create field that will show warnings 
        self.createFieldWarning()

        #entry fields
        facebook_url_label = Label(button_frame, text='URL of friend to Scrape:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        facebook_url_label.place(relx=0.04, rely=0, relwidth=0.25, relheight=0.1)
        enter_visibility_label = Label(button_frame, text='visible/invisible :', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_visibility_label.place(relx=0.09, rely=0.12, relwidth=0.25, relheight=0.1)

        self.facebook_url_entry = Entry(button_frame, width=59)
        self.facebook_url_entry.grid (row=1,column=1,pady=5, ipady=20)
        self.facebook_visibility_entry = Entry(button_frame, width=59)
        self.facebook_visibility_entry.grid (row=2,column=1,pady=5, ipady=20)

        #send button
        self.createButton(button_frame, text='Enter', command=self.send_facebook_url, 
                            row=3,col=1)

        # back button
        back = self.getPageChangeFunction('FacebookPage')
        self.createButton(button_frame, text='Back', command=back, row=4,col=0)

    #TODO: function to pass arguments to Ashraf's scripts
    def send_facebook_url(self):
        facebook_url_entry = self.facebook_url_entry.get()
        facebook_visibility_entry = self.facebook_visibility_entry.get()

        if facebook_url_entry =='' or facebook_visibility_entry =='':
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            print (facebook_url_entry)
            print (facebook_visibility_entry)
            print("NOT SENDING ARGUMENTS TO PUBLIC scraper")
            self.changePages('FacebookPage')

    def createFieldWarning(self):
        self.field_warning_label = Label (self.button_frame,text='',font=('orbitron', 13),
                                           fg='white', bg='#80c1ff', anchor='n')
        self.field_warning_label.grid(row=4,column=1,pady=5, ipady=20)
