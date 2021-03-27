from tkinter import PhotoImage, Label, Button, Frame
from CommonFrame import CommonFrame

#-------------------------------------------Selection--------------------------------------------------
class MenuPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        super().setSubHeading('Main Menu')

        #selection label
        selection_label = Label(self, text='Please make a selection', font=('orbitron', 15), fg='white', bg='#0077e6', anchor='w' )
        selection_label.pack(fill='x')

        #buttons/frame to select which application to Scrape
        button_frame = Frame(self,bg='#80c1ff')
        button_frame.pack(fill='both', expand=True)

        #spear fish symbol
        fish_image = PhotoImage (file='images/fish.png')
        fish_label = Label(button_frame, image=fish_image)
        fish_label.place(relx=0.6, rely=0)
        fish_label.image = fish_image

        #facebook
        def scrape_Facebook():
            controller.show_frame('FacebookPage')

        ScrapeFacebook_button = Button(button_frame, text='Scrape Facebook', command=scrape_Facebook, relief='raised',borderwidth=3, width=50,height=5)
        ScrapeFacebook_button.grid (row=0,column=0, pady=5)

        #twitter
        def scrape_Twittter():
            controller.show_frame('TwitterPage')

        ScrapeTwitter_button = Button(button_frame, text='Scrape Twitter', command=scrape_Twittter, relief='raised',borderwidth=3, width=50,height=5)
        ScrapeTwitter_button.grid (row=1,column=0, pady=5)

        #exit
        def exit():
            controller.show_frame('LoginPage')

        exit_button = Button(button_frame, text='Exit', command=exit, relief='raised',borderwidth=3, width=50,height=5)
        exit_button.grid (row=2,column=0, pady=5)