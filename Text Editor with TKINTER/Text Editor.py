import tkinter as tk
from tkinter import filedialog

def open_file():
    types = [('Text file', '*.txt'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(initialdir='.', title='Open file', filetypes=types)
    if filepath:
        with open(filepath, 'r') as file:
            text.delete('1.0', tk.END)  # Clear previous text
            text.insert(tk.END, file.read())  # Insert file content into text widget

def save_file():
    types = [('Text file', '*.txt'), ('All files', '*.*')]
    filepath = filedialog.asksaveasfilename(filetypes=types, initialdir='.')
    if filepath:
        file_content = text.get('1.0', tk.END)
        with open(filepath, 'w') as file:
            file.write(file_content)

root = tk.Tk()
root.title("Text Editor")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

button_open = tk.Button(frame, text="OPEN", command=open_file)
button_open.grid(column=0, row=0, padx=5, pady=5)

button_saveas = tk.Button(frame, text="SAVE AS", command=save_file)
button_saveas.grid(column=1, row=0, padx=5, pady=5)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

text = tk.Text(frame)
text.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

root.mainloop()
