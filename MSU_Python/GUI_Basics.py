#! /usr/bin/python3


import tkinter as tk
from tkinter import ttk

def Click():
	root.title("You Clicked the button")

def Exit():
	root.destroy()

root = tk.Tk() # Create tkinter object 

root.configure(bg='white')

root.title("Test 12344567") # create root windows title

root.geometry("300x200") # Set width and height of the root window. 

# create a frame:
frame = ttk.Frame(root, style='My.TFrame', padding="10 10 10 10") # Create a frame object. 
frame.pack(fill=tk.BOTH, expand=True)
'''
Description
Makes the component visible. To make acomponent automatically resize itself vertically and horizontally to
fill the parent component, you can set the fill argument to BOTH and the expand argument to True.
'''

# Create a button:
button1 = tk.Button(frame, text="Click me!", command=Click)
button2 = tk.Button(frame, text="End Me", command=Exit)

# Labels:
investmentLabel = ttk.Label(frame, text="Monthly Investment")
investmentLabel.pack

investmentText = tk.StringVar()
INVEStmentEntry= ttk.Entry(frame, width=25, textvariable=investmentText)

investmentText.set("")
investment = investmentText.get()


button2.pack() # Notice how order of pack matters. 
button1.pack()



root.mainloop() 
"""
 Makes the root window visible and starts an event processing
loop that allows a program to handle events that occur on the window. You need to call this method after all other code that
sets up the root window.
"""

