from tkinter import Frame, Label, PhotoImage 

# creates picture in the frame
def createPictureInFrame(button_frame: Frame, image_path: str):
    image = PhotoImage (file=image_path)
    image_label = Label(button_frame, image=image)
    image_label.place(relx=0.6, rely=0)
    image_label.image = image