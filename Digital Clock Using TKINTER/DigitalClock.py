import tkinter as tk
from tkinter import Label, Tk 
import time
root = tk.Tk() 
root.title(" VINIEK Digital Clock") 
root.geometry("420x150") 
root.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "blue"
foreground= "purple"
border_width = 25

label = Label(root, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
root.mainloop()