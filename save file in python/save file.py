from tkinter import*
from tkinter import filedialog

def save_file():
    type = [('Text file', '*.txt'),('All files', '*.*')]
    file = entry.get()

    path = filedialog.asksaveasfilename(filetypes=type, initialdir='.')
    file_save = open(path, 'w')
    file_save.write(file)
    file_save.close()
    
root = Tk()
button = Button(root, text="save", command=save_file)
button.grid(row=1, column=0)

entry = Entry(root)
entry.grid(row=0, column=1)

label = Label(root, text='Enter text ypu want to save')
label.grid(row=0, column=0)
root.mainloop()