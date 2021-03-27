from tkinter import Label, Button, Frame
from CommonFrame import CommonFrame

# Page for Facebook selection
class FacebookPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        super().setSubHeading('Facebook')

        #subheadings
        #Facebook selection path
        super().createLeftSubHeading('Please make a selection')
        super().createRightSubHeading('Previous Page: Main menu')

        #buttons/frame to select which application to Scrape
        button_frame = super().createAndGetButtonFrame()

        #Facebook symbol
        super().createPictureInFrame(button_frame, 'images/facebook.png')

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