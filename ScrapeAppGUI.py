#GUI application for spear phishing tool
#Abdullah Chattha mar 22/2021
#imports
import tkinter as tk
from FacebookChatPhisher import *
from tweetGenerator import createCorpus
from tweetGenerator import generateResponse
from FacebookPost import post
import time

#code
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, Facebook_page, Twitter_page,facebook_public_page,facebook_private_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#------------------------------------------Login------------------------------------------------------------
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#0077e6')
        self.controller = controller

        #window attributes
        self.controller.title ("Spear Phishing Tool")
        self.controller.state ('normal')
        self.controller.iconphoto (False, tk.PhotoImage (file='images/scraper.png'))

        #heading for start page
        heading_label = tk.Label(self, text='Spear Phishing Tool', font=('orbitron', 45,'bold'), fg='white', bg='#0077e6')
        heading_label.pack(pady=25)

        #password entry
        space_label = tk.Label(self,height=4, bg='#0077e6')
        space_label.pack()

        password_label=tk.Label(self,text='Enter password', font=('orbitron', 13), bg='#0077e6', fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password,font=('orbitron', 12), width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

        #password enter button and checker
        def check_password():
            if my_password.get() == '123':
                my_password.set('')
                incorrect_password_label['text']=''
                controller.show_frame('MenuPage')
            else:
                incorrect_password_label['text']='Incorrect Password'


        enter_button= tk.Button(self, text='Enter', command=check_password, relief='raised', borderwidth=3, width=40, height=3 )
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label (self,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)

        #bottom frame for time
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        #python develop sentence
        python_dev_label = tk.Label(bottom_frame, text='Developed with: ', font=('orbitron', 12,'bold'))
        python_dev_label.place(relx=0)

        #python symbol
        python_image = tk.PhotoImage (file='images/python.png')
        python_label = tk.Label(bottom_frame, image=python_image)
        python_label.place(relx=0.11)
        python_label.image = python_image

        #time bar at the bottom
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron-Bold',12))
        time_label.pack (side='right')

        tick ()

#-------------------------------------------Selection-------------------------------------------------------
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#0077e6')
        self.controller = controller

        #heading for start page
        heading_label = tk.Label(self, text='Spear Phishing Tool', font=('orbitron', 45,'bold'), fg='white', bg='#0077e6')
        heading_label.pack(pady=25)

        #main menu heading
        main_menu_label = tk.Label(self, text='Main Menu', font=('orbitron', 13), fg='white', bg='#0077e6' )
        main_menu_label.pack()

        #selection label
        selection_label = tk.Label(self, text='Please make a selection', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label.pack(fill='x')

        #bottom frame for time
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        #python develop sentence
        python_dev_label = tk.Label(bottom_frame, text='Developed with: ', font=('orbitron', 12,'bold'))
        python_dev_label.place(relx=0)

        #python symbol
        python_image = tk.PhotoImage (file='images/python.png')
        python_label = tk.Label(bottom_frame, image=python_image)
        python_label.place(relx=0.11)
        python_label.image = python_image

        #time bar at the bottom
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron-Bold',12))
        time_label.pack (side='right')

        tick ()

        #buttons/frame to sleect which application to Scrape
        button_frame = tk.Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #spear fish symbol
        fish_image = tk.PhotoImage (file='images/fish.png')
        fish_label = tk.Label(button_frame, image=fish_image)
        fish_label.place(relx=0.6, rely=0)
        fish_label.image = fish_image

        #facebook
        def scrape_Facebook():
            controller.show_frame('Facebook_page')

        ScrapeFacebook_button = tk.Button(button_frame, text='Scrape Facebook', command=scrape_Facebook, relief='raised',borderwidth=3, width=50,height=5)
        ScrapeFacebook_button.grid (row=0,column=0, pady=5)

        #twitter
        def scrape_Twittter():
            controller.show_frame('Twitter_page')

        ScrapeTwitter_button = tk.Button(button_frame, text='Scrape Twitter', command=scrape_Twittter, relief='raised',borderwidth=3, width=50,height=5)
        ScrapeTwitter_button.grid (row=1,column=0, pady=5)

        #exit
        def exit():
            controller.show_frame('StartPage')

        exit_button = tk.Button(button_frame, text='Exit', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=2,column=0, pady=5)

#-------------------------------------------facebook pages--------------------------------------------------
class Facebook_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#0077e6')
        self.controller = controller

        #heading
        heading_label = tk.Label(self, text='Spear Phishing Tool', font=('orbitron', 45,'bold'), fg='white', bg='#0077e6')
        heading_label.pack(pady=25)

        #facebook heading
        facebook_menu_label = tk.Label(self, text='Facebook', font=('orbitron', 13), fg='white', bg='#0077e6' )
        facebook_menu_label.pack()

        #bottom frame for time/dev statment
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        #python develop sentence
        python_dev_label = tk.Label(bottom_frame, text='Developed with: ', font=('orbitron', 12,'bold'))
        python_dev_label.place(relx=0)

        #python symbol
        python_image = tk.PhotoImage (file='images/python.png')
        python_label = tk.Label(bottom_frame, image=python_image)
        python_label.place(relx=0.11)
        python_label.image = python_image

        #time bar at the bottom
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron-Bold',12))
        time_label.pack (side='right')

        tick ()

        #subheadings
        #facebook selection path
        selection_label_facebook = tk.Label(self, text='Please make a selection', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label_facebook.pack(fill='x')

        path_label_facebook = tk.Label(self, text='Previous Page: Main menu', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        path_label_facebook.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)


        #buttons/frame to sleect which application to Scrape
        button_frame = tk.Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #facebook symbol
        facebook_image = tk.PhotoImage (file='images/facebook.png')
        facebook_label = tk.Label(button_frame, image=facebook_image)
        facebook_label.place(relx=0.6, rely=0)
        facebook_label.image = facebook_image

        #buttons for facebook public/private
        def scrape_public_facebook():
            controller.show_frame('facebook_public_page')

        Scrape_public_Facebook_button = tk.Button(button_frame, text='Public Facebook', command=scrape_public_facebook, relief='raised',borderwidth=3, width=50,height=5)
        Scrape_public_Facebook_button.grid (row=0,column=0, pady=5)

        def scrape_private_facebook():
            controller.show_frame('facebook_private_page')

        Scrape_private_Facebook_button = tk.Button(button_frame, text='Private Facebook', command=scrape_private_facebook, relief='raised',borderwidth=3, width=50,height=5)
        Scrape_private_Facebook_button.grid (row=1,column=0, pady=5)

        #back button
        def exit():
            controller.show_frame('MenuPage')

        exit_button = tk.Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=2,column=0, pady=5)

class facebook_public_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#0077e6')
        self.controller = controller

        #heading
        heading_label = tk.Label(self, text='Spear Phishing Tool', font=('orbitron', 45,'bold'), fg='white', bg='#0077e6')
        heading_label.pack(pady=25)

        #facebook heading
        facebook_menu_label = tk.Label(self, text='Public Facebook', font=('orbitron', 13), fg='white', bg='#0077e6' )
        facebook_menu_label.pack()

        #bottom frame for time
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        #python develop sentence
        python_dev_label = tk.Label(bottom_frame, text='Developed with: ', font=('orbitron', 12,'bold'))
        python_dev_label.place(relx=0)

        #python symbol
        python_image = tk.PhotoImage (file='images/python.png')
        python_label = tk.Label(bottom_frame, image=python_image)
        python_label.place(relx=0.11)
        python_label.image = python_image

        #time bar at the bottom
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron-Bold',12))
        time_label.pack (side='right')

        tick ()

        #subheadings
        #facebook selection path
        selection_label_facebook = tk.Label(self, text='Please enter fields', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label_facebook.pack(fill='x')

        path_label_facebook = tk.Label(self, text='Previous Page: Facebook', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        path_label_facebook.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)

        #frame for buttons
        button_frame = tk.Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #facebook symbol
        facebook_image = tk.PhotoImage (file='images/facebook.png')
        facebook_label = tk.Label(button_frame, image=facebook_image)
        facebook_label.place(relx=0.6, rely=0)
        facebook_label.image = facebook_image

        #function to pass arguments to ashrafs scripts
        def send_facebook_url(facebook_url_entry, facebook_visibility_entry):
            if facebook_url_entry =='' or facebook_visibility_entry =='':
                field_warning_label['text']='*Please fill all fields*'
            else:
                print (facebook_url_entry)
                print (facebook_visibility_entry)
                controller.show_frame('Facebook_page')


        field_warning_label = tk.Label (button_frame,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        field_warning_label.grid(row=4,column=1,pady=5, ipady=20)

        #entry feilds
        facebook_url_label = tk.Label(button_frame, text='URL of friend to Scrape:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        facebook_url_label.place(relx=0.04, rely=0, relwidth=0.25, relheight=0.1)
        enter_visibility_label = tk.Label(button_frame, text='visible/invisible :', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_visibility_label.place(relx=0.09, rely=0.12, relwidth=0.25, relheight=0.1)

        facebook_url_entry = tk.Entry(button_frame, width=59)
        facebook_url_entry.grid (row=1,column=1,pady=5, ipady=20)
        facebook_visibility_entry = tk.Entry(button_frame, width=59)
        facebook_visibility_entry.grid (row=2,column=1,pady=5, ipady=20)

        #send button
        send_button = tk.Button(button_frame, text='Enter', command= lambda:send_facebook_url(facebook_url_entry.get(),facebook_visibility_entry.get()) , relief='raised',borderwidth=3, width=50,height=5)
        send_button.grid (row=3,column=1, pady=5)

        #back button
        def exit():
            controller.show_frame('Facebook_page')

        exit_button = tk.Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=4,column=0, pady=5)

class facebook_private_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#0077e6')
        self.controller = controller

        #heading
        heading_label = tk.Label(self, text='Spear Phishing Tool', font=('orbitron', 45,'bold'), fg='white', bg='#0077e6')
        heading_label.pack(pady=25)

        #facebook heading
        facebook_menu_label = tk.Label(self, text='Private Facebook', font=('orbitron', 13), fg='white', bg='#0077e6' )
        facebook_menu_label.pack()

        #bottom frame for time
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        #python develop sentence
        python_dev_label = tk.Label(bottom_frame, text='Developed with: ', font=('orbitron', 12,'bold'))
        python_dev_label.place(relx=0)

        #python symbol
        python_image = tk.PhotoImage (file='images/python.png')
        python_label = tk.Label(bottom_frame, image=python_image)
        python_label.place(relx=0.11)
        python_label.image = python_image

        #time bar at the bottom
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron-Bold',12))
        time_label.pack (side='right')

        tick ()

        #subheadings
        #facebook selection path
        selection_label_facebook = tk.Label(self, text='Please enter fields', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label_facebook.pack(fill='x')

        path_label_facebook = tk.Label(self, text='Previous Page: Facebook', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        path_label_facebook.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)

        #frame for buttons/entry feilds
        button_frame = tk.Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #facebook symbol
        facebook_image = tk.PhotoImage (file='images/facebook.png')
        facebook_label = tk.Label(button_frame, image=facebook_image)
        facebook_label.place(relx=0.6, rely=0)
        facebook_label.image = facebook_image

        #function to pass arguments to ashrafs scripts
        def send_facebook_quad(facebook_email_entry, facebook_username_entry, facebook_password_entry, facebook_numberOfFriends_entry):
            if facebook_email_entry =='' or facebook_username_entry =='' or facebook_password_entry =='' or facebook_numberOfFriends_entry =='' :
                status_label['text']='*Please fill all fields*'
            else:

                #run Ashraf main.py script #linux path is the tor download path----------------------------
                driver = loginToFacebook(pathToTorInstallation, facebook_email_entry , facebook_password_entry)
                time.sleep(8)

                FULLHTMLPAGE = getFriendsListHTMLPage(driver, facebook_username_entry)
                # will parse the HTML page to obtain hrefs of friends.
                friendURLS = parseHTML(FULLHTMLPAGE, "friendsurls", 1)

                scrapeLikePages(driver, friendURLS, int(facebook_numberOfFriends_entry))
                #------------------------------------------------------------------------------------------
                controller.show_frame('Facebook_page')

        #warning symbol if any feild missing
        status_label = tk.Label (button_frame,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        status_label.grid(row=5,column=1,pady=5, ipady=20)

        #labels
        enter_email_label = tk.Label(button_frame, text='Email used for Facebook:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_email_label.place(relx=0.04, rely=0, relwidth=0.25, relheight=0.1)
        enter_username_label = tk.Label(button_frame, text='Facebook username:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_username_label.place(relx=0.06, rely=0.12, relwidth=0.25, relheight=0.1)
        enter_password_label = tk.Label(button_frame, text='Facebook Password:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_password_label.place(relx=0.06, rely=0.24, relwidth=0.25, relheight=0.1)
        enter_friends_label = tk.Label(button_frame, text='Number of friends:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        enter_friends_label.place(relx=0.08, rely=0.36, relwidth=0.25, relheight=0.1)

        #entry feilds
        facebook_email_entry = tk.Entry(button_frame, width=59)
        facebook_email_entry.grid (row=0,column=1,pady=5, ipady=20)
        facebook_username_entry = tk.Entry(button_frame, width=59)
        facebook_username_entry.grid (row=1,column=1,pady=5,ipady=20)
        facebook_password_entry = tk.Entry(button_frame, width=59)
        facebook_password_entry.grid (row=2,column=1,pady=5,ipady=20)
        facebook_numberOfFriends_entry = tk.Entry(button_frame, width=59)
        facebook_numberOfFriends_entry.grid (row=3,column=1,pady=5, ipady=20)

        #send button
        send_button = tk.Button(button_frame, text='Enter', command= lambda:send_facebook_quad(facebook_email_entry.get(),facebook_username_entry.get(), facebook_password_entry.get(), facebook_numberOfFriends_entry.get()) , relief='raised',borderwidth=3, width=50,height=5)
        send_button.grid (row=4,column=1, pady=5)

        #back button
        def exit():
            controller.show_frame('Facebook_page')

        exit_button = tk.Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=5,column=0, pady=5)

#-------------------------------------------twitter pages----------------------------------------------------
class Twitter_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#0077e6')
        self.controller = controller

        #heading
        heading_label = tk.Label(self, text='Spear Phishing Tool', font=('orbitron', 45,'bold'), fg='white', bg='#0077e6')
        heading_label.pack(pady=25)

        #twitter heading
        twitter_menu_label = tk.Label(self, text='Twitter', font=('orbitron', 13), fg='white', bg='#0077e6' )
        twitter_menu_label.pack()

        #bottom frame for time
        bottom_frame = tk.Frame(self,relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        #python develop sentence
        python_dev_label = tk.Label(bottom_frame, text='Developed with: ', font=('orbitron', 12,'bold'))
        python_dev_label.place(relx=0)

        #python symbol
        python_image = tk.PhotoImage (file='images/python.png')
        python_label = tk.Label(bottom_frame, image=python_image)
        python_label.place(relx=0.11)
        python_label.image = python_image

        #time bar at the bottom
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron-Bold',12))
        time_label.pack (side='right')

        tick ()

        #subheadings
        #twitter selection path
        selection_label_twitter = tk.Label(self, text='Please enter fields', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label_twitter.pack(fill='x')

        path_label_twitter = tk.Label(self, text='Previous Page: Main menu', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        path_label_twitter.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)

        #frame for buttons
        button_frame = tk.Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #twitter symbol
        twitter_image = tk.PhotoImage (file='images/twitter.png')
        twitter_label = tk.Label(button_frame, image=twitter_image)
        twitter_label.place(relx=0.6, rely=0)
        twitter_label.image = twitter_image

        #function to pass to ashrafs scripts
        def send_twitter_handle (twitter_handle_entry):
            if twitter_handle_entry =='':
                field_warning_label['text']='*Please fill all fields*'
            else:
                #call Abdullah a part
                createCorpusForUser (twitter_handle_entry)
                generateTweet (twitter_handle_entry, 'example.com')

                #print(twitter_handle_entry)
                controller.show_frame('MenuPage')

        field_warning_label = tk.Label (button_frame,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        field_warning_label.grid(row=2,column=1,pady=5, ipady=20)

        #entry fields
        twitter_handle_label = tk.Label(button_frame, text='Twitter handle of account:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        twitter_handle_label.place(relx=0.04, rely=0, relwidth=0.25, relheight=0.1)

        twitter_handle_entry = tk.Entry(button_frame, width=59)
        twitter_handle_entry.grid (row=0,column=1,pady=5, ipady=20)

        #send button
        send_button = tk.Button(button_frame, text='Enter', command= lambda:send_twitter_handle(twitter_handle_entry.get()) , relief='raised',borderwidth=3, width=50,height=5)
        send_button.grid (row=1,column=1, pady=5)

        #exit
        def exit():
            controller.show_frame('MenuPage')

        exit_button = tk.Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=2,column=0, pady=5)

#------------------------------------------End of Pages----------------------------------------------------
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
