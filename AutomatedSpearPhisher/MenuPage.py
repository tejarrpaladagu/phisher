from tkinter import Label, Button, Frame
from CommonFrame import CommonFrame

#-------------------------------------------Selection--------------------------------------------------
class MenuPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        super().setSubHeading('Main Menu')

        #selection label
        super().createLeftSubHeading('Please make a selection')
        

        #buttons/frame to select which application to Scrape
        button_frame = super().createAndGetButtonFrame()

        #spear fish symbol
        super().createPictureInFrame(button_frame, 'images/fish.png')

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