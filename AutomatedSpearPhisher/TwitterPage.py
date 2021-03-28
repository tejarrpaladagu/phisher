from tkinter import Label, Button, Frame, Entry
from tweetGenerator import createCorpusForUser
from tweetGenerator import generateTweet
from CommonFrame import CommonFrame
from helpers import *

#-------------------------------------------Twitter page----------------------------------------------
class TwitterPage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)           

        #subheadings
        setSubHeading(self, 'Twitter')
        #twitter selection path
        createLeftSubHeading(self, 'Please enter fields')
        createRightSubHeading(self, 'Previous Page: Main menu')

        #frame for buttons
        self.createButtonFrame()
        button_frame = self.getButtonFrame()
        button_manager = ButtonManager(button_frame, controller)

        #twitter symbol
        createPictureInFrame(button_frame, 'images/twitter.png')
        self.field_warning_label = createFieldWarning(button_frame, row=2, col=1)

        #entry fields
        self.setUpLabelGrid(start_row=0, start_col=0)
        self.setUpEntryGrid(start_row=0, start_col=1)
        self.addLabelWithEntry('Twitter handle of account:', 'twitter_handle_entry')

        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.send_twitter_handle, row=1, col=1)

        #back button
        button_manager.createChangePageButton(page_name='MenuPage', text='Back', row=2,col=0)

    #function to pass to Ashraf's scripts
    def send_twitter_handle (self):
        twitter_handle_entry = self.getValueOfEntry('twitter_handle_entry')
        if twitter_handle_entry =='':
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            #call tweet generator
            createCorpusForUser (twitter_handle_entry)
            generateTweet (twitter_handle_entry, 'example.com')

            #print(twitter_handle_entry)
            self.changePages('MenuPage')