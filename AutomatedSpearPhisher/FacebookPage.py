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
        
        #Facebook symbol
        createPictureInFrame(button_frame, 'images/facebook.png')

        # create selection button to go to pages
        self.createChangePageButton('FacebookPublicPage', 'Public Facebook')
        self.createChangePageButton('FacebookPrivatePage', 'Private Facebook')
        self.createChangePageButton('MenuPage', 'Back')
