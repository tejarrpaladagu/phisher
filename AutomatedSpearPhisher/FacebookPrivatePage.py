from tkinter import Label, Button, Entry
from CommonFrame import CommonFrame
from config import pathToTorInstallation
from FacebookChatPhisher import *
# TODO: add posting and phishing text generation 
from FacebookPost import post
import phishingTextGenerator 

class FacebookPrivatePage(CommonFrame):

    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        

        #subheadings
        self.setSubHeading('Private Facebook')
        #Facebook selection path
        self.createLeftSubHeading('Please enter fields')
        self.createRightSubHeading('Previous Page: Facebook')

        #frame for buttons/entry fields
        self.createButtonFrame()
        button_frame = self.getButtonFrame()

        #Facebook symbol
        self.createPictureInFrame('images/facebook.png')

        #function to pass arguments to Ashraf's scripts
        def send_facebook_quad(facebook_email_entry, facebook_username_entry, facebook_password_entry, facebook_numberOfFriends_entry):
            if facebook_email_entry =='' or facebook_username_entry =='' or facebook_password_entry =='' or facebook_numberOfFriends_entry =='' :
                status_label['text']='*Please fill all fields*'
            else:

                #run Ashraf's main.py script ----------------------------
                driver = loginToFacebook(pathToTorInstallation, facebook_email_entry , facebook_password_entry)
                time.sleep(8)

                FULLHTMLPAGE = getFriendsListHTMLPage(driver, facebook_username_entry)
                # will parse the HTML page to obtain hrefs of friends.
                friendURLS = parseHTML(FULLHTMLPAGE, "friendsurls", 1)

                scrapeLikePages(driver, friendURLS, int(facebook_numberOfFriends_entry))
                #------------------------------------------------------------------------------------------
                controller.show_frame('FacebookPage')

        #warning symbol if any field missing
        status_label = Label (button_frame,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        status_label.grid(row=5,column=1,pady=5, ipady=20)

        #labels
        enter_email_label = Label(button_frame, text='Email used for Facebook:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_email_label.place(relx=0.04, rely=0, relwidth=0.25, relheight=0.1)
        enter_username_label = Label(button_frame, text='Facebook username:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_username_label.place(relx=0.06, rely=0.12, relwidth=0.25, relheight=0.1)
        enter_password_label = Label(button_frame, text='Facebook Password:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_password_label.place(relx=0.06, rely=0.24, relwidth=0.25, relheight=0.1)
        enter_friends_label = Label(button_frame, text='Number of friends:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_friends_label.place(relx=0.08, rely=0.36, relwidth=0.25, relheight=0.1)

        #entry fields
        facebook_email_entry = Entry(button_frame, width=59)
        facebook_email_entry.grid (row=0,column=1,pady=5, ipady=20)
        facebook_username_entry = Entry(button_frame, width=59)
        facebook_username_entry.grid (row=1,column=1,pady=5,ipady=20)
        facebook_password_entry = Entry(button_frame, width=59)
        facebook_password_entry.grid (row=2,column=1,pady=5,ipady=20)
        facebook_numberOfFriends_entry = Entry(button_frame, width=59)
        facebook_numberOfFriends_entry.grid (row=3,column=1,pady=5, ipady=20)

        #send button
        send_button = Button(button_frame, text='Enter', command= lambda:send_facebook_quad(facebook_email_entry.get(),facebook_username_entry.get(), facebook_password_entry.get(), facebook_numberOfFriends_entry.get()) , relief='raised',borderwidth=3, width=50,height=5)
        send_button.grid (row=4,column=1, pady=5)

        #back button
        back = self.getPageChangeFunction('FacebookPage')
        self.createButton(button_frame, text='Back', command=back, row=5,col=0)

