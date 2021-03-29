from tkinter import Label, Button, Entry
from tkinter.ttk import Combobox
from tkinter import filedialog
from CommonFrame import CommonFrame
from config import tor_installation_path
from FacebookChatPhisher import *
# TODO: add posting option
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
        self.addButtons(button_frame)

    def setFile(self):
        ftypes = [('Executables files', '*.exe'), ('All files', '*')]
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = ftypes)
        self.entry_manager.setValueOfEntry('driver_path', filename)
        
    # add in buttons in the frame
    def addButtons(self, button_frame):
        button_manager = ButtonManager(button_frame, self.changePages)
        button_manager.createButton(button_frame, text='Open', command=self.setFile, row=5, col=0, width=15, height=4)
        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.scrapePrivateFacebook, row=7, col=1)
        #back button
        button_manager.createChangePageButton(page_name='FacebookPage', text='Back', row=8,col=0)

    # drop-down select browser
    def addBrowserSelector(self, button_frame):
        self.browser_selector = Combobox(button_frame, values=getSupportedBrowser())
        self.browser_selector.grid(row=6, column=1)
        self.browser_selector.current(0)

    def addEnteries(self, entry_manager):
        entry_manager.addLabelWithEntry('Email used for Facebook:', 'email')
        entry_manager.addLabelWithEntry('Facebook username:', 'username')
        entry_manager.addLabelWithEntry('Facebook Password:', 'password')
        entry_manager.addLabelWithEntry('Number of friends:', 'numberOfFriends')
        entry_manager.addLabelWithEntry('Path to driver:', 'driver_path', sticky_label='we')

    #function to pass arguments to Ashraf's scripts
    def scrapePrivateFacebook(self):
        entry_manager = self.entry_manager
        email = entry_manager.getValueOfEntry('email')
        username = entry_manager.getValueOfEntry('username')
        password = entry_manager.getValueOfEntry('password')
        numberOfFriends = entry_manager.getValueOfEntry('numberOfFriends')
        driver_path =  entry_manager.getValueOfEntry('driver_path')
        browser_mode = SUPPORTED_BROWSER.get( self.browser_selector.get())

        if email =='' or username ==''\
            or password =='' or numberOfFriends =='' :
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            # login to Facebook
            driver = getDriver(driver_path, browser_mode, tor_installation_path)
            loginToFacebook(driver, email , password)
            sleep(8)
            # get list of friend's pages
            FULLHTMLPAGE = getFriendsListHTMLPage(driver, username)
            # extract the URL to their page
            friendURLS = parseHTML(FULLHTMLPAGE, 'friendsurls', 1)
            # scrape and store their likes pages
            # TODO: figure out how to store files in output directory
            scrapeLikePages(driver, friendURLS, int(numberOfFriends))
            # create phishing text based on created like pages
            # TODO: pass in output and input directory
            phishingTextGenerator.main()
            self.changePages('FacebookPage')
