# Import Required Module
from tkinter import *
from tkinter.ttk import *

# Create Root Object
root = Tk()
# Set Geometry(widthxheight)
root.geometry('500x500')

# Create style Object
style = Style()

style.configure('TButton', font =
			('calibri', 20, 'bold'),
					borderwidth = '4')

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'Red')],
					background = [('active', 'black')])

# button 1
btn1 = Button(root, text = 'Quit !', command = root.destroy)
btn1.grid(row = 0, column = 3, padx = 100)


btn2 = Button(root, text = 'Click me !', command = None)
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

# Execute Tkinter
root.mainloop()
