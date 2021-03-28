from tkinter import Label, Button, Entry
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
        button_manager = ButtonManager(button_frame, self.changePages)
        
        #Facebook symbol
        createPictureInFrame(button_frame, 'images/facebook.png')
        #create field that will show warnings 
        self.field_warning_label = createFieldWarning(button_frame, row=4, col=1)

        #create entry fields and their label
        self.entry_manager = EntryManager(button_frame, start_row=1, label_col=0, entry_col=1)
        self.entry_manager.addLabelWithEntry('URL of friend to Scrape:', 'facebook_url_entry')
        self.entry_manager.addLabelWithEntry('visible/invisible :', 'facebook_visibility_entry')

        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.send_facebook_url, row=3, col=1)

        # back button
        button_manager.createChangePageButton(page_name='FacebookPage', text='Back', row=4,col=0)

    #TODO: function to pass arguments to Ashraf's scripts
    def send_facebook_url(self):
        entry_manager = self.entry_manager
        facebook_url_entry = entry_manager.getValueOfEntry('facebook_url_entry')
        facebook_visibility_entry = entry_manager.getValueOfEntry('facebook_visibility_entry')

        if facebook_url_entry =='' or facebook_visibility_entry =='':
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            print (facebook_url_entry)
            print (facebook_visibility_entry)
            print('NOT SENDING ARGUMENTS TO PUBLIC scraper')
            self.changePages('FacebookPage')
