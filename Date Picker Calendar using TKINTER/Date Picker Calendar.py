
import tkinter as tk
import tkcalendar as Calendar

root=tk.Tk()
root.title("VINIEK CALENDER")

cal=Calendar.Calendar(master=root,selectmode="day",year=2024,month=12,day=19)
cal.pack(pady=20)

def grad_date():
    label_date.config(text="The selected date is:"+cal.get_date())

button=tk.Button(master=root,text="Get Date",command=grad_date).pack(pady=20)
label_date=tk.Label(master=root,text=" ").pack(pady=20)
root.mainloop()