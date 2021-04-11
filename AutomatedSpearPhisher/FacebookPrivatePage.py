from tkinter.ttk import Combobox
from tkinter import filedialog, Checkbutton, IntVar
from CommonFrame import CommonFrame
from config import tor_installation_path
from FacebookChatPhisher import *
from FacebookPost import post
import phishingTextGenerator 
from time import sleep
from helpers import *

class FacebookPrivatePage(CommonFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        #subheadings
        setSubHeading(self, 'Private Facebook')
        #Facebook selection path
        createLeftSubHeading(self, 'Please enter fields')
        createRightSubHeading(self, 'Previous Page: Facebook')
        #frame for buttons/entry fields
        self.createButtonFrame()
        button_frame = self.getButtonFrame()
        #Facebook symbol
        createPictureInFrame(button_frame, 'images/facebook.png')
        # field to show warnings
        self.field_warning_label = createFieldWarning(button_frame, row=8, col=1)
        # creating typeable fields 
        self.entry_manager = EntryManager(button_frame, start_row=1, label_col=0, entry_col=1)
        self.addEnteries(self.entry_manager)
        self.addBrowserSelector(button_frame)
        self.addPostingCheckBox(button_frame)
        self.addButtons(button_frame)

    def setFile(self):
        ftypes = [('Executables files', '*.exe'), ('All files', '*')]
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = ftypes)
        self.entry_manager.setValueOfEntry('driverPath', filename)
        
    # add in buttons in the frame
    def addButtons(self, button_frame):
        button_manager = ButtonManager(button_frame, self.changePages)
        button_manager.createButton(button_frame, text='Open', command=self.setFile, row=5, col=0, width=15, height=3)
        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.scrapePrivateFacebook, row=7, col=1)
        #back button
        button_manager.createChangePageButton(page_name='FacebookPage', text='Back', row=8,col=0)

    # drop-down select browser
    def addBrowserSelector(self, button_frame):
        self.browser_selector = Combobox(button_frame, values=getSupportedBrowser(), width=35,height=15, font=('orbitron', 15))
        self.browser_selector.grid(row=6, column=1)
        self.browser_selector.current(0)

    def addPostingCheckBox(self, button_frame):
        self.shouldPost = IntVar()
        poster_box = Checkbutton(button_frame, text = "Post To Facebook", 
                                 variable=self.shouldPost)
        poster_box.grid(row=6, column=0)

    def addEnteries(self, entry_manager):
        entry_manager.addLabelWithEntry('Email used for Facebook:', 'email')
        entry_manager.addLabelWithEntry('Facebook Password:', 'password', show='*')
        entry_manager.addLabelWithEntry('Your Facebook Username:', 'username')
        entry_manager.addNumericalEntryWithLabel('Number of Friends to Scrape:', 'numberOfFriends')
        entry_manager.addLabelWithEntry('Path to driver:', 'driverPath', sticky_label='we')

    #function to pass arguments to Ashraf's scripts
    def scrapePrivateFacebook(self):
        entry_manager = self.entry_manager
        email = entry_manager.getValueOfEntry('email')
        password = entry_manager.getValueOfEntry('password')
        username = entry_manager.getValueOfEntry('username')
        numberOfFriends = entry_manager.getValueOfEntry('numberOfFriends')
        driverPath =  entry_manager.getValueOfEntry('driverPath')
        browserMode = SUPPORTED_BROWSER.get( self.browser_selector.get())

        if email =='' or username ==''\
            or password =='' or numberOfFriends =='' :
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            inputPath = "Resources/facebook"
            outputPath = "Output/facebook"
            # login to Facebook
            driver = getDriver(driverPath, browserMode, tor_installation_path)
            loginToFacebook(driver, email , password)
            sleep(8)
            # get list of friend's pages
            FULLHTMLPAGE = getFriendsListHTMLPage(driver, username)
            # extract the URL to their page
            friendURLS = parseFriendsPage(FULLHTMLPAGE)
            # scrape and store their likes pages
            scrapeLikePages(driver, friendURLS, int(numberOfFriends), inputPath)
            # create phishing text based on created like pages
            phishingTextGenerator.main(inputPath, outputPath)
            if self.shouldPost.get() == 1:
                self.postToFacebook(driver, friendURLS, outputPath)
            self.changePages('FacebookPage')
                
    def postToFacebook(self, driver, friendURLS: list, outputPath : str):
        for i in range(len(friendURLS)):
            friendURL = friendURLS[i]
            filepath = f"{outputPath}/message{i}.txt"
            with open(filepath, "r", encoding='utf-8') as f:
                message = f.read()
                post(driver, friendURL, message)


