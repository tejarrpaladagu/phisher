from CommonFrame import CommonFrame
from helpers import * 

# Page for Facebook selection
class FacebookPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)

        #subheadings
        setSubHeading(self, 'Facebook')
        #Facebook selection path
        createLeftSubHeading(self, 'Please make a selection')
        createRightSubHeading(self, 'Previous Page: Main menu')

        #buttons/frame to select which application to Scrape
        self.createButtonFrame()
        button_frame = self.getButtonFrame()
        self.addButtons(button_frame)

        #Facebook symbol
        createPictureInFrame(button_frame, 'images/facebook.png')

    def addButtons(self, button_frame):
        button_manager = ButtonManager(button_frame, self.changePages)
        # create selection button to go to pages
        button_manager.autoCreateChangePageButton('FacebookPublicPage', 'Public Facebook')
        button_manager.autoCreateChangePageButton('FacebookPrivatePage', 'Private Facebook')
        button_manager.autoCreateChangePageButton('MenuPage', 'Back')