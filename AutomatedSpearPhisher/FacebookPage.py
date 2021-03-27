from tkinter import PhotoImage, Label, Button, Frame
from CommonFrame import CommonFrame

# Page for Facebook selection
class FacebookPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        super().setSubHeading('Facebook')

        #subheadings
        #Facebook selection path
        selection_label_facebook = Label(self, text='Please make a selection', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label_facebook.pack(fill='x')

        path_label_facebook = Label(self, text='Previous Page: Main menu', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='e' )
        path_label_facebook.place(relx=0.75, rely=0.13, relwidth=0.25, relheight=0.15)


        #buttons/frame to select which application to Scrape
        button_frame = Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #Facebook symbol
        facebook_image = PhotoImage (file='images/facebook.png')
        facebook_label = Label(button_frame, image=facebook_image)
        facebook_label.place(relx=0.6, rely=0)
        facebook_label.image = facebook_image

        #buttons for Facebook public/private
        def scrape_public_facebook():
            controller.show_frame('FacebookPublicPage')

        Scrape_public_Facebook_button = Button(button_frame, text='Public Facebook', command=scrape_public_facebook, relief='raised',borderwidth=3, width=50,height=5)
        Scrape_public_Facebook_button.grid (row=0,column=0, pady=5)

        def scrape_private_facebook():
            controller.show_frame('FacebookPrivatePage')

        Scrape_private_Facebook_button = Button(button_frame, text='Private Facebook', command=scrape_private_facebook, relief='raised',borderwidth=3, width=50,height=5)
        Scrape_private_Facebook_button.grid (row=1,column=0, pady=5)

        #back button
        def exit():
            controller.show_frame('MenuPage')

        exit_button = Button(button_frame, text='Back', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=2,column=0, pady=5)