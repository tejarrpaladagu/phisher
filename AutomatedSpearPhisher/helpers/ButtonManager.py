from tkinter import Frame, Button
from typing import Callable
from functools import partial

# Handles creation of button to a given - allows button to be added automatically and increment row
# Also simplifies page changing
class ButtonManager:
    def __init__(self, button_frame: Frame, changePages: Callable[[Frame, str], None]):
        if button_frame==None:
            raise ValueError
        self.changePages = changePages
        self.button_frame = button_frame
        # used to automatically insert buttons
        self.button_row = 0
        self.button_col = 0
        self.last_button_row = 0

    #  Get back last row we created a button. This makes it easier to place objects
    def getLastButtonRow(self)-> int:
        return self.last_button_row

    # Make a button that runs a given function when pressed 
    def createButton(self, button_frame: Frame, text: str, command: Callable[[], None], 
                   row: int, col: int, style='raised', borderwidth=3, width=50,height=5, sticky=''):
        button = Button(button_frame, text=text, command=command,
                        relief=style,borderwidth=borderwidth, width=width,height=height)
        button.grid (row=row,column=col, pady=5, sticky=sticky)
        self.last_button_row = max(row, self.last_button_row)
    
    # add button to main button frame - and go to new row 
    def autoAddButton(self, text: str, command : Callable[[], None], style='raised', 
                      borderwidth=3, width=50,height=5):
        button_frame = self.button_frame
        self.createButton(button_frame, text, command, self.button_row, 
                       self.button_col, style, borderwidth, width, height)
        self.button_row+=1

    # page changing functions 
    def getPageChangeFunction(self, page_name: str) -> Callable[[], None]:
        return partial(self.changePages, page_name)

    # Convenience function to change pages
    def autoCreateChangePageButton(self, page_name: str, text: str):
        change_page_func = self.getPageChangeFunction(page_name)
        self.autoAddButton(text, change_page_func)

    # Create a button that changes pages but you can pass in rows and column
    def createChangePageButton(self, page_name: str, text: str, row: int, col: int):
        change_page_func = self.getPageChangeFunction(page_name)
        self.createButton(self.button_frame, text, change_page_func, row, col)