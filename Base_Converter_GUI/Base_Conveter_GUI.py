import tkinter as tk

# Main window
root = tk.Tk()

root.title("Base Converter")
root.geometry("300x500")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Parent widget for the buttons
numbers_frame = tk.Frame(root)
numbers_frame.grid(row=1, column=0)

button7 = tk.Button(numbers_frame, text='7', width = 5, height = 5)
button7.grid(row=0, column=0, sticky = "nsew")

button8 = tk.Button(numbers_frame, text='8', width = 5, height = 5)
button8.grid(row=0, column=1, sticky = "nsew")

button9 = tk.Button(numbers_frame, text='9', height = 5, width = 5)
button9.grid(row=0, column=2, sticky = "nsew")

button4 = tk.Button(numbers_frame, text='4')
button4.grid(row=1, column=0, sticky = "nsew")

button5 = tk.Button(numbers_frame, text='5')
button5.grid(row=1, column=1, sticky = "nsew")

button6 = tk.Button(numbers_frame, text='6')
button6.grid(row=1, column=2, sticky = "nsew")

button7 = tk.Button(numbers_frame, text='1')
button7.grid(row=2, column=0, sticky = "nsew")

button8 = tk.Button(numbers_frame, text='2')
button8.grid(row=2, column=1, sticky = "nsew")

button9 = tk.Button(numbers_frame, text='3')
button9.grid(row=2, column=2, sticky = "nsew")

button0 = tk.Button(numbers_frame, text='0')
button0.grid(row=3, column=0, sticky = "nsew")

button_decimal = tk.Button(numbers_frame, text='.')
button_decimal.grid(row=3, column=1, sticky = "nsew")

# Text box
input = tk.Entry(root)
input.grid(row = 0, column = 1)

root.mainloop()