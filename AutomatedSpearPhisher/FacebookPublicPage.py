from CommonFrame import CommonFrame
# TODO: add face book public scraper
# TODO: make sure posting works on public scraper as well 
from FacebookPost import post
from helpers import *

class FacebookPublicPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)

        #subheadings
        setSubHeading(self, 'Public Facebook')
        #Facebook selection path
        createLeftSubHeading(self, 'Please enter fields')
        createRightSubHeading(self, 'Previous Page: Facebook')

        #frame for buttons
        self.createButtonFrame()
        button_frame = self.getButtonFrame()
        #Facebook symbol
        createPictureInFrame(button_frame, 'images/facebook.png')
        #create entry fields and their label
        self.entry_manager = EntryManager(button_frame, start_row=1, label_col=0, entry_col=1)
        self.addEnteries(self.entry_manager)   
        last_entry_row = self.entry_manager.getLastEntryRow()
        # create buttons
        last_button_row = self.addButtons(button_frame, last_entry_row+1)
        #create field that will show warnings 
        self.field_warning_label = createFieldWarning(button_frame, row=last_button_row, col=1)

    #TODO: function to pass arguments to Ashraf's scripts
    def scrapePublicFacebook(self):
        entry_manager = self.entry_manager
        facebook_url = entry_manager.getValueOfEntry('facebook_url')
        facebook_visibility = entry_manager.getValueOfEntry('facebook_visibility')

        if not entry_manager.allFieldsFilled():
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            print (facebook_url)
            print (facebook_visibility)
            print('NOT SENDING ARGUMENTS TO PUBLIC scraper')
            self.changePages('FacebookPage')

    # add in buttons in the frame and get back last row that we have a button
    def addButtons(self, button_frame, button_row):
        button_manager = ButtonManager(button_frame, self.changePages)
        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.scrapePublicFacebook, row=button_row, col=1)
        # back button
        button_manager.createChangePageButton(page_name='FacebookPage', text='Back', row=button_row+1,col=0)
        return button_manager.getLastButtonRow()

    def addEnteries(self, entry_manager):
        entry_manager.addLabelWithEntry('URL of friend to Scrape:', 'facebook_url')
        entry_manager.addLabelWithEntry('visible/invisible :', 'facebook_visibility')