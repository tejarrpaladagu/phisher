from tkinter import Label, Button, Entry
from CommonFrame import CommonFrame

class FacebookPublicPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        self.setSubHeading('Public Facebook')

        #subheadings
        #Facebook selection path
        self.createLeftSubHeading('Please enter fields')
        self.createRightSubHeading('Previous Page: Facebook')

        #frame for buttons
        self.createButtonFrame()
        button_frame = self.button_frame
        
        #Facebook symbol
        self.createPictureInFrame('images/facebook.png')

        #function to pass arguments to Ashraf's scripts
        def send_facebook_url(facebook_url_entry, facebook_visibility_entry):
            if facebook_url_entry =='' or facebook_visibility_entry =='':
                field_warning_label['text']='*Please fill all fields*'
            else:
                print (facebook_url_entry)
                print (facebook_visibility_entry)
                controller.show_frame('FacebookPage')


        field_warning_label = Label (button_frame,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        field_warning_label.grid(row=4,column=1,pady=5, ipady=20)

        #entry fields
        facebook_url_label = Label(button_frame, text='URL of friend to Scrape:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        facebook_url_label.place(relx=0.04, rely=0, relwidth=0.25, relheight=0.1)
        enter_visibility_label = Label(button_frame, text='visible/invisible :', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_visibility_label.place(relx=0.09, rely=0.12, relwidth=0.25, relheight=0.1)

        facebook_url_entry = Entry(button_frame, width=59)
        facebook_url_entry.grid (row=1,column=1,pady=5, ipady=20)
        facebook_visibility_entry = Entry(button_frame, width=59)
        facebook_visibility_entry.grid (row=2,column=1,pady=5, ipady=20)

        #send button
        send_button = Button(button_frame, text='Enter', command= lambda:send_facebook_url(facebook_url_entry.get(),facebook_visibility_entry.get()) , relief='raised',borderwidth=3, width=50,height=5)
        send_button.grid (row=3,column=1, pady=5)

        #back button
        def exit():
            controller.show_frame('FacebookPage')

        exit_button = Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=4,column=0, pady=5)
