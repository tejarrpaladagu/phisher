from tkinter import Label, Button, Frame, Entry
from CommonFrame import CommonFrame

#-------------------------------------------Twitter page----------------------------------------------
class TwitterPage(CommonFrame):

    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)           
        super().setSubHeading('Twitter')

        #subheadings
        #twitter selection path
        selection_label_twitter = Label(self, text='Please enter fields', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label_twitter.pack(fill='x')

        path_label_twitter = Label(self, text='Previous Page: Main menu', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        path_label_twitter.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)

        #frame for buttons
        button_frame = super().createAndGetButtonFrame()

        #twitter symbol
        super().createPictureInFrame(button_frame, 'images/twitter.png')

        #function to pass to Ashraf's scripts
        def send_twitter_handle (twitter_handle_entry):
            if twitter_handle_entry =='':
                field_warning_label['text']='*Please fill all fields*'
            else:
                #call Abdullah a part
                createCorpusForUser (twitter_handle_entry)
                generateTweet (twitter_handle_entry, 'example.com')

                #print(twitter_handle_entry)
                controller.show_frame('MenuPage')

        field_warning_label = Label (button_frame,text='',font=('orbitron', 13),fg='white', bg='#80c1ff', anchor='n')
        field_warning_label.grid(row=2,column=1,pady=5, ipady=20)

        #entry fields
        twitter_handle_label = Label(button_frame, text='Twitter handle of account:', font=('orbitron', 15), fg='white', bg='#80c1ff',anchor='w' )
        twitter_handle_label.place(relx=0.04, rely=0, relwidth=0.25, relheight=0.1)

        twitter_handle_entry = Entry(button_frame, width=59)
        twitter_handle_entry.grid (row=0,column=1,pady=5, ipady=20)

        #send button
        send_button = Button(button_frame, text='Enter', command= lambda:send_twitter_handle(twitter_handle_entry.get()) , relief='raised',borderwidth=3, width=50,height=5)
        send_button.grid (row=1,column=1, pady=5)

        #exit
        def exit():
            controller.show_frame('MenuPage')

        exit_button = Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=2,column=0, pady=5)