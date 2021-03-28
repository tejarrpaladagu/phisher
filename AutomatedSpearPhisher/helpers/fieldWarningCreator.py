from tkinter import Frame, Label

# field warning create a text field that will show a user-friendly error
def createFieldWarning(button_frame: Frame, row: int, col: int) -> Label:
        field_warning_label = Label (button_frame,text='',font=('orbitron', 13),
                                           fg='white', bg='#80c1ff', anchor='s')
        field_warning_label.grid(row=row,column=col,pady=5, ipady=20)
        return field_warning_label