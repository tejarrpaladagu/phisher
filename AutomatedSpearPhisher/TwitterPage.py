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
        #twitter symbol
        createPictureInFrame(button_frame, 'images/twitter.png')
        #entry fields
        self.entry_manager = EntryManager(button_frame, start_row=0, label_col=0, entry_col=1)
        self.addEnteries(self.entry_manager)
        last_entry_row = self.entry_manager.getLastEntryRow()
        last_button_row = self.addButtons(button_frame, last_entry_row+1)
        self.field_warning_label = createFieldWarning(button_frame, row=last_button_row, col=1)


    #function to pass to Ashraf's scripts
    def sendTwitterHandle (self):
        entry_manager = self.entry_manager
        twitter_handle = entry_manager.getValueOfEntry('twitter_handle')
        twitter_url = entry_manager.getValueOfEntry('twitter_url')
        num_scrape_tweets = entry_manager.getValueOfEntry('num_scrape_tweets')
        num_tweets = entry_manager.getValueOfEntry('num_tweets')
        tweets_folder = "Resources/tweets"
        gen_tweets_folder = "Output/tweets"

        if not entry_manager.allFieldsFilled():
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            #call tweet generator
            createCorpusForUser (twitter_handle, tweets_folder, int(num_scrape_tweets))
            generateTweet (twitter_handle, twitter_url, gen_tweets_folder,\
                            tweets_folder, int(num_tweets))

            #print(twitter_handle)
            self.changePages('MenuPage')

    # add in buttons in the frame and get back last row that we have a button
    def addButtons(self, button_frame, button_row):
        button_manager = ButtonManager(button_frame, self.changePages)
        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.sendTwitterHandle, row=button_row, col=1)
        #back button
        button_manager.createChangePageButton(page_name='MenuPage', text='Back', row=button_row+1,col=0)
        return button_manager.getLastButtonRow()


    def addEnteries(self, entry_manager):
        entry_manager.addLabelWithEntry('Twitter handle of account:', 'twitter_handle')
        entry_manager.addLabelWithEntry('Phishing URL:', 'twitter_url')
        entry_manager.addNumericalEntryWithLabel('Tweets to Scrape', 'num_scrape_tweets')
        entry_manager.setValueOfEntry('num_scrape_tweets', str(5000))
        entry_manager.addNumericalEntryWithLabel('Tweets to generate', 'num_tweets')
        entry_manager.setValueOfEntry('num_tweets', str(10))

