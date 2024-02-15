from tkinter import*
from tkinter import filedialog
root = Tk()
def open_file():
    types= [('Text file', '*.txt'),('Png files','*.png'),('All files','*.*')]
    path = filedialog.askopenfilename(initialdir='.',title='Open file', filetypes=types)
    
    file = open(path, 'r')
    label.configure(text=file.read())
    
    
    
    

button = Button(root, text='njeriiii', command=open_file)
button.grid(row=0, column=0)
label = Label(root)
label.grid(row=1, column=0)

root.mainloop()