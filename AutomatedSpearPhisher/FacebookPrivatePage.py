from tkinter import PhotoImage, Label, Button, Frame, Entry
from CommonFrame import CommonFrame

class FacebookPrivatePage(CommonFrame):

    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        super().setSubHeading('Private Facebook')

        #subheadings
        #Facebook selection path
        selection_label_facebook = Label(self, text='Please enter fields', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label_facebook.pack(fill='x')

        path_label_facebook = Label(self, text='Previous Page: Facebook', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        path_label_facebook.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)

        #frame for buttons/entry fields
        button_frame = Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #Facebook symbol
        facebook_image = PhotoImage (file='images/facebook.png')
        facebook_label = Label(button_frame, image=facebook_image)
        facebook_label.place(relx=0.6, rely=0)
        facebook_label.image = facebook_image

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
        def exit():
            controller.show_frame('FacebookPage')

        exit_button = Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=5,column=0, pady=5)
