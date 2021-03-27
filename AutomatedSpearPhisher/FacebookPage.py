from CommonFrame import CommonFrame

# Page for Facebook selection
class FacebookPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        self.setSubHeading('Facebook')

        #subheadings
        #Facebook selection path
        self.createLeftSubHeading('Please make a selection')
        self.createRightSubHeading('Previous Page: Main menu')

        #buttons/frame to select which application to Scrape
        self.createButtonFrame()

        #Facebook symbol
        self.createPictureInFrame('images/facebook.png')

        # create selection button to go to pages
        self.createChangePageButton('FacebookPublicPage', 'Public Facebook')
        self.createChangePageButton('FacebookPrivatePage', 'Private Facebook')
        self.createChangePageButton('MenuPage', 'Back')
