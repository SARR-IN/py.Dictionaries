import webbrowser
from tkinter import *
root = Tk()
root.title("WebBrowser")
root.geometry("300×200")
def google():
    webbrowser.open("www.google.com")
    mygoogle = Button(root, text="open Google", command=google).pack(pady=20)
    root.mainloop()
