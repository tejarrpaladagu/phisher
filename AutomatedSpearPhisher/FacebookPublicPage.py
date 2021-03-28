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

        #Facebook symbol
        createPictureInFrame(button_frame, 'images/facebook.png')
        #create field that will show warnings 
        self.field_warning_label = createFieldWarning(button_frame, row=4, col=1)

        #create entry fields and their label
        self.setUpLabelGrid(start_row=1, start_col=0)
        self.setUpEntryGrid(start_row=1, start_col=1)
        self.addLabelWithEntry('URL of friend to Scrape:', 'facebook_url_entry')
        self.addLabelWithEntry('visible/invisible :', 'facebook_visibility_entry')

        #send button
        self.createButton(button_frame, text='Enter', command=self.send_facebook_url, row=3, col=1)

        # back button
        back = self.getPageChangeFunction('FacebookPage')
        self.createButton(button_frame, text='Back', command=back, row=4,col=0)

    #TODO: function to pass arguments to Ashraf's scripts
    def send_facebook_url(self):
        facebook_url_entry = self.getValueOfEntry('facebook_url_entry')
        facebook_visibility_entry = self.getValueOfEntry('facebook_visibility_entry')

        if facebook_url_entry =='' or facebook_visibility_entry =='':
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            print (facebook_url_entry)
            print (facebook_visibility_entry)
            print('NOT SENDING ARGUMENTS TO PUBLIC scraper')
            self.changePages('FacebookPage')
