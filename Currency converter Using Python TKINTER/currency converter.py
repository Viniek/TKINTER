import tkinter as tk

root = tk.Tk()
root.title("Shillings Converter to Dollars")
root.resizable(width=False, height=False)
root.configure(bg="blue")
def convertshs():
    try:
        shs = float(entry_shs.get())
        dollar = shs * 159.50
        label_shsresult.config(text=f"Result: {dollar:.2f} USD")
    except ValueError:
        label_shsresult.config(text="Please enter a valid number.")

def convertusd():
    try:
        usd = float(entry_usd.get())
        shs = usd / 159.50
        label_usdresult.config(text=f"Result: {shs:.2f} Shs")
    except ValueError:
        label_usdresult.config(text="Please enter a valid number.")

# Shillings Frame
frame_shs = tk.Frame(master=root, bg="blue")
frame_shs.grid(row=0, column=0, padx=10, pady=10)

label_shs = tk.Label(master=frame_shs, text="Shs", bg="blue")
label_shs.grid(row=0, column=0)

entry_shs = tk.Entry(master=frame_shs, width=6)
entry_shs.grid(row=0, column=1)

button_convert_shs = tk.Button(master=frame_shs, text="Convert", command=convertshs)
button_convert_shs.grid(row=1, column=0, columnspan=2, pady=10)

label_shsresult = tk.Label(master=frame_shs, text="Result:")
label_shsresult.grid(row=2, column=0, columnspan=2)

# Dollars Frame
frame_usd = tk.Frame(master=root, bg="blue")
frame_usd.grid(row=0, column=1, padx=10, pady=10)

label_usd = tk.Label(master=frame_usd, text="USD", bg="blue")
label_usd.grid(row=0, column=0)

entry_usd = tk.Entry(master=frame_usd, width=6)
entry_usd.grid(row=0, column=1)

button_convert_usd = tk.Button(master=frame_usd, text="Convert", command=convertusd)
button_convert_usd.grid(row=1, column=0, columnspan=2, pady=10)

label_usdresult = tk.Label(master=frame_usd, text="Result:")
label_usdresult.grid(row=2, column=0, columnspan=2)

root.mainloop()
