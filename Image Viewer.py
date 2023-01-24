from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons")

# The below code is used to change icons
# The parameters passed in the bracket is image address
root.iconbitmap(r"C:\Users\hp\Documents\Experimental Images")

myimg1 = ImageTk.PhotoImage(Image.open(r"C:\Users\hp\Documents\Experimental Images\A Letter.png"))
myimg2 = ImageTk.PhotoImage(Image.open(r"C:\Users\hp\Documents\Experimental Images\D Letter.png"))
myimg3 = ImageTk.PhotoImage(Image.open(r"C:\Users\hp\Documents\Experimental Images\R Letter.png"))
myimg4 = ImageTk.PhotoImage(Image.open(r"C:\Users\hp\Documents\Experimental Images\S Letter.png"))

imgList = [myimg1, myimg2, myimg3, myimg4]

status = Label(root, text="Image 1 of " + str(len(imgList)), bd=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=myimg1)
myLabel.grid(row=0, column=0, columnspan=3)


def forward(imgnum):
    global myLabel
    global button_forward
    global button_back
    myLabel.grid_forget()
    myLabel = Label(image=imgList[imgnum-1])
    button_forward = Button(root, text="forward", command=lambda: forward(imgnum+1))
    button_back = Button(root, text="back", command=lambda: back(imgnum-1))

    if imgnum == 4:
        button_forward = Button(root, text="forward", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(imgnum) + " of " + str(len(imgList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(imgnum):
    global myLabel
    global button_forward
    global button_back
    myLabel.grid_forget()
    myLabel = Label(image=imgList[imgnum - 1])
    button_forward = Button(root, text="forward", command=lambda: forward(imgnum + 1))
    button_back = Button(root, text="back", command=lambda: back(imgnum - 1))
    myLabel.grid(row=0, column=0, columnspan=3)

    if imgnum == 1:
        button_back = Button(root, text="Back", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(imgnum) + " of " + str(len(imgList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="Back", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text="forward", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
