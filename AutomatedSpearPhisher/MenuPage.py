from CommonFrame import CommonFrame

#-------------------------------------------Selection--------------------------------------------------
class MenuPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        #Set center subheading
        self.setSubHeading('Main Menu')
        #selection label
        self.createLeftSubHeading('Please make a selection')
        #buttons/frame to select which application to Scrape
        self.createButtonFrame()
        #spear fish symbol
        self.createPictureInFrame('images/fish.png')

        # create selection button to go to pages
        self.createChangePageButton('FacebookPage', 'Scrape Facebook')
        self.createChangePageButton('TwitterPage', 'Scrape Twitter')
        self.createChangePageButton('LoginPage', 'Exit')