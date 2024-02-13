import tkinter as tk
root=tk.Tk()
root.title("Viniek Temperature Converter")
root.resizable(width=False,height=False)


def convert_fahrenheit():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (5/9) * (fahrenheit - 32)
    label_result_fahrenheit["text"] = f"{round(celsius, 2)}"

def convert_celsius():
    celsius = float(entry_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    label_result_celsius["text"] = f"{round(fahrenheit, 2)} °F"


# Fahrenheit Frame
frame_fahrenheit = tk.Frame(master=root,bg="blue")
frame_fahrenheit.grid(row=0, column=0)

label_fahrenheit = tk.Label(master=frame_fahrenheit, text="Fahrenheit temperature:")
label_fahrenheit.grid(row=0, column=0)

entry_fahrenheit = tk.Entry(master=frame_fahrenheit)
entry_fahrenheit.grid(row=0, column=1)

btn_convert_fahrenheit = tk.Button(master=frame_fahrenheit, text="Convert", command=convert_fahrenheit)
btn_convert_fahrenheit.grid(row=1, column=0, columnspan=2)

label_result_fahrenheit = tk.Label(master=frame_fahrenheit, text="Result")
label_result_fahrenheit.grid(row=2, column=0, columnspan=2)

# Celsius Frame
frame_celsius = tk.Frame(master=root,bg="blue")
frame_celsius.grid(row=0, column=1)

label_celsius = tk.Label(master=frame_celsius, text="Celsius temperature:")
label_celsius.grid(row=0, column=0)

entry_celsius = tk.Entry(master=frame_celsius)
entry_celsius.grid(row=0, column=1)

btn_convert_celsius = tk.Button(master=frame_celsius, text="Convert", command=convert_celsius)
btn_convert_celsius.grid(row=1, column=0, columnspan=2)

label_result_celsius = tk.Label(master=frame_celsius, text="Result")
label_result_celsius.grid(row=2, column=0, columnspan=2)

root.mainloop()
