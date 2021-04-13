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
        # creating typeable fields 
        self.entry_manager = EntryManager(button_frame, start_row=0, label_col=0, entry_col=1)
        self.addEnteries(self.entry_manager)
        last_entry_row = self.entry_manager.getLastEntryRow()
        self.addBrowserSelector(button_frame, last_entry_row+1)
        self.addPostingCheckBox(button_frame, last_entry_row+1)
        ''' The buttons will be placed after the entries, the 
            browser selector and posting check-box
        '''
        button_rows = last_entry_row +2
        last_button_row =  self.addButtons(button_frame, button_rows)
        # field to show warnings
        self.field_warning_label = createFieldWarning(button_frame, row=last_button_row, col=1)

    def setFile(self):
        ftypes = [('Executables files', '*.exe'), ('All files', '*')]
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = ftypes)
        self.entry_manager.setValueOfEntry('driver_path', filename)
        
    # add in buttons in the frame and get back last row that we have a button
    def addButtons(self, button_frame, button_rows: int):
        button_manager = ButtonManager(button_frame, self.changePages)
        driver_path_row = self.entry_manager.getEntryGridInfo('driver_path')['row']
        # This button is associated with the entry that control the browser driver path
        button_manager.createButton(button_frame, text='Open', command=self.setFile, row=driver_path_row, col=0, width=15, height=3)
        #send button
        button_manager.createButton(button_frame, text='Enter', command=self.scrapePrivateFacebook, row=button_rows, col=1)
        #back button
        button_manager.createChangePageButton(page_name='FacebookPage', text='Back', row=button_rows+1,col=0)
        return button_manager.getLastButtonRow()

    # drop-down select browser
    def addBrowserSelector(self, button_frame, browser_row: int):
        self.browser_selector = Combobox(button_frame, values=getSupportedBrowser(), width=35,height=15, font=('orbitron', 15))
        self.browser_selector.grid(row=browser_row, column=1)
        self.browser_selector.current(0)

    def addPostingCheckBox(self, button_frame, check_box_row: int):
        self.shouldPost = IntVar()
        poster_box = Checkbutton(button_frame, text = "Post To Facebook", 
                                 variable=self.shouldPost)
        poster_box.grid(row=check_box_row, column=0)

    def addEnteries(self, entry_manager):
        entry_manager.addLabelWithEntry('Email used for Facebook:', 'email')
        entry_manager.addLabelWithEntry('Facebook Password:', 'password', show='*')
        entry_manager.addLabelWithEntry('Your Facebook Username:', 'username')
        entry_manager.addNumericalEntryWithLabel('Number of Friends to Scrape:', 'num_friends')
        entry_manager.addLabelWithEntry('Path to driver:', 'driver_path', sticky_label='we')

    #function to pass arguments to Ashraf's scripts
    def scrapePrivateFacebook(self):
        entry_manager = self.entry_manager
        email = entry_manager.getValueOfEntry('email')
        password = entry_manager.getValueOfEntry('password')
        username = entry_manager.getValueOfEntry('username')
        num_friends = entry_manager.getValueOfEntry('num_friends')
        driver_path =  entry_manager.getValueOfEntry('driver_path')
        browser_mode = SUPPORTED_BROWSER.get(self.browser_selector.get())

        if not entry_manager.allFieldsFilled() :
            self.field_warning_label['text']='*Please fill all fields*'
        else:
            inputPath = "Resources/facebook"
            outputPath = "Output/facebook"
            # login to Facebook
            driver = getDriver(driver_path, browser_mode, tor_installation_path)
            loginToFacebook(driver, email , password)
            sleep(8)
            # get list of friend's pages
            FULLHTMLPAGE = getFriendsListHTMLPage(driver, username)
            # extract the URL to their page
            friendURLS = parseFriendsPage(FULLHTMLPAGE)
            # scrape and store their likes pages
            scrapeLikePages(driver, friendURLS, int(num_friends), inputPath)
            # create phishing text based on created like pages
            phishingTextGenerator.main(inputPath, outputPath)
            if self.shouldPostToFacebook():
                self.postToFacebook(driver, friendURLS, outputPath)
            self.changePages('FacebookPage')
                
    def shouldPostToFacebook(self)-> bool:
        return self.shouldPost.get() == 1

    def postToFacebook(self, driver, friendURLS: list, outputPath : str):
        for i in range(len(friendURLS)):
            friendURL = friendURLS[i]
            filepath = f"{outputPath}/message{i}.txt"
            with open(filepath, "r", encoding='utf-8') as f:
                message = f.read()
                post(driver, friendURL, message)
                sleep(3)


