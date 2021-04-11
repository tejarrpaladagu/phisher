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
        self.addButtons(button_frame)
        self.field_warning_label = createFieldWarning(button_frame, row=6, col=1)

        #entry fields
        self.entry_manager = EntryManager(button_frame, start_row=0, label_col=0, entry_col=1)
        self.addEnteries(self.entry_manager)

    #function to pass to Ashraf's scripts
    def sendTwitterHandle (self):
        entry_manager = self.entry_manager
        twitter_handle = entry_manager.getValueOfEntry('twitter_handle')
        twitter_url = entry_manager.getValueOfEntry('twitter_url')
        num_scrape_tweets = entry_manager.getValueOfEntry('num_scrape_tweets')
        num_tweets = entry_manager.getValueOfEntry('num_tweets')
        tweets_folder = "Resources/tweets"
        gen_tweets_folder = "Output/tweets"

        if twitter_handle =='' or twitter_url == '' or \
            num_scrape_tweets =='' or num_tweets == '':
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            #call tweet generator
            createCorpusForUser (twitter_handle, tweets_folder, int(num_scrape_tweets))
            generateTweet (twitter_handle, twitter_url, gen_tweets_folder,\
                            tweets_folder, int(num_tweets))

            #print(twitter_handle)
            self.changePages('MenuPage')

    def addButtons(self, button_frame):
        button_manager = ButtonManager(button_frame, self.changePages)
        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.sendTwitterHandle, row=4, col=1)
        #back button
        button_manager.createChangePageButton(page_name='MenuPage', text='Back', row=6,col=0)

    def addEnteries(self, entry_manager):
        entry_manager.addLabelWithEntry('Twitter handle of account:', 'twitter_handle')
        entry_manager.addLabelWithEntry('Phishing URL:', 'twitter_url')
        entry_manager.addNumericalEntryWithLabel('Tweets to Scrape', 'num_scrape_tweets')
        entry_manager.setValueOfEntry('num_scrape_tweets', str(5000))
        entry_manager.addNumericalEntryWithLabel('Tweets to generate', 'num_tweets')
        entry_manager.setValueOfEntry('num_tweets', str(10))

