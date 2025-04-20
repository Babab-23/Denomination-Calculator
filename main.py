#Import necessary libraries
from tkinter import *
#Setting Up Main window
root=Tk()
root.geometry("400x300")
root.title("main")
#Function to open New (Top Level) Window
def topwin():
    #Setting Up Top window
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    #Adding a label widget to Top Window
    l2=Label(top,text="This is toplevel window")
    l2.pack()
    top.mainloop()
#Adding a label and button widget to Root (Main) window
l=Label(root,text="This is root window")
btn=Button(root,text="Click here to open another window",command=topwin)
#Arranging widgets
l.pack()
btn.pack()
root.mainloop()