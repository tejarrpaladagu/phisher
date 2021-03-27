#GUI application for spear phishing tool
#Abdullah Chattha mar 22/2021
#imports
from tkinter import Tk, Frame
from LoginPage import LoginPage
from MenuPage import MenuPage
from FacebookPage import FacebookPage
from TwitterPage import TwitterPage
from FacebookPublicPage import FacebookPublicPage
from FacebookPrivatePage import FacebookPrivatePage

#Parent class which handles rendering in Tkinter
class AutomatedSpearPhisherApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        '''
            the container is where we'll stack a bunch of frames
            on top of each other, then the one we want visible
            will be raised above the others
        '''
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, MenuPage, FacebookPage, TwitterPage, FacebookPublicPage,FacebookPrivatePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            '''
                put all of the pages in the same location;
                the one on the top of the stacking order
                will be the one that is visible.
            '''
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = AutomatedSpearPhisherApp()
    app.mainloop()
