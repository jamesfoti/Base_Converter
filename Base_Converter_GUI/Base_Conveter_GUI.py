import tkinter as tk

# Main window
root = tk.Tk()
root.title("Base Converter")
root.geometry("300x500")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

array = []
# Functions
def Display_Number(num):
    input.insert(tk.END, num)
    array.append(num)
    a = int(''.join(map(str,array)))
    print(a)

def Clear_Entry():
    input.delete(0, tk.END)
    input.insert(0, 0)

def Button_Layout():
    # Number buttons
    """
    Input layout:
        7 8 9
        4 5 6
        1 2 3
        0 . =
    """
    button7 = tk.Button(numbers_frame, text=7, command=lambda: Display_Number(7)).grid(row=0, column=0, sticky="nsew")
    button8 = tk.Button(numbers_frame, text=8, command=lambda: Display_Number(8)).grid(row=0, column=1, sticky="nsew")
    button9 = tk.Button(numbers_frame, text=9, command=lambda: Display_Number(9)).grid(row=0, column=2, sticky="nsew")

    button4 = tk.Button(numbers_frame, text=4, command=lambda: Display_Number(4)).grid(row=1, column=0, sticky="nsew")
    button5 = tk.Button(numbers_frame, text=5, command=lambda: Display_Number(5)).grid(row=1, column=1, sticky="nsew")
    button6 = tk.Button(numbers_frame, text=6, command=lambda: Display_Number(6)).grid(row=1, column=2, sticky="nsew")

    button1 = tk.Button(numbers_frame, text=1, command=lambda: Display_Number(1)).grid(row=2, column=0, sticky="nsew")
    button2 = tk.Button(numbers_frame, text=2, command=lambda: Display_Number(2)).grid(row=2, column=1, sticky="nsew")
    button3 = tk.Button(numbers_frame, text=3, command=lambda: Display_Number(3)).grid(row=2, column=2, sticky="nsew")

    zero_button = tk.Button(numbers_frame, text="0", command=lambda: Display_Number(0)).grid(row=3, column=0,
                                                                                             sticky="nsew")
    decimal_button = tk.Button(numbers_frame, text='.').grid(row=3, column=1, sticky="nsew")
    clear_button = tk.Button(numbers_frame, text="Clear", command=lambda: Clear_Entry()).grid(row=4, column=0,
                                                                                              sticky="nsew")

# Parent widget for the buttons
numbers_frame = tk.Frame(root)
numbers_frame.grid(row=1, column=0)

input = tk.Entry(root)
input.grid(row = 0, column = 0)

output = tk.Entry(root)
output.grid(row = 0, column = 1)


Button_Layout()


root.mainloop()