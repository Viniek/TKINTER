import random
import tkinter as tk
root=tk.Tk()
root.resizable(1,0)
root.configure(bg="blue")

def roll():
    label_result["text"]=int(random.randint(1,6))

btn_roll=tk.Button(text="Roll",bg="violet",command=roll)
btn_roll.grid(column=0, row=0)

label_result=tk.Label()
label_result.grid(column=0, row=1)
root.mainloop()
    