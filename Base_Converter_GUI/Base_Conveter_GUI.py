from tkinter import *

# Main window
root = Tk()
root.title("Base Converter")
root.geometry("500x500")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

frame = Frame(root)
Grid.rowconfigure(root,  0, weight = 1)
Grid.columnconfigure(root, 0, weight = 1)
frame.grid(row=1, column=0, sticky=N+S+E+W)
grid = Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

array = []
# Functions
def Display_Number(num):
    entry1.insert(END, num)
    array.append(num)
    a = int(''.join(map(str,array)))
    print(a)

def Clear_Entry():
    entry1.delete(0, END)
    entry1.insert(0, 0)

entry1 = Entry(root, font = "20").place(relx = .25, rely = .10, height=50, anchor = N)
entry2 = Entry(root, font = "20").place(relx = .75, rely = .10, height=50, anchor = N)

convert_button = Button(root, text= "CONVERT", font = "20").place(relx = .5, rely = .22, width = 90, height = 50, anchor = N)

# Convert-from buttons
decimal_button1 = Button(root, text= "Decimal", font = "20").place(relx = .25, rely = .25, width = 100, height = 35, anchor = CENTER)
binary_button1 = Button(root, text= "Binary", font = "20").place(relx = .25, rely = .33, width = 100, height = 35, anchor = CENTER)
hex_button1 = Button(root, text= "Hexadecimal", font = "20").place(relx = .25, rely = .41, width = 100, height = 35, anchor = CENTER)

# Convert-to buttons
decimal_button2 = Button(root, text= "Decimal", font = "20").place(relx = .75, rely = .25, width = 100, height = 35, anchor = CENTER)
binary_button2 = Button(root, text= "Binary", font = "20").place(relx = .75, rely = .33, width = 100, height = 35, anchor = CENTER)
hex_button2 = Button(root, text= "Hexadecimal", font = "20").place(relx = .75, rely = .41, width = 100, height = 35, anchor = CENTER)

button7 = Button(frame, text=7, command=lambda: Display_Number(7)).grid(row=3, column=0, sticky=N+S+E+W)
button8 = Button(frame, text=8, command=lambda: Display_Number(8)).grid(row=3, column=1, sticky=N+S+E+W)
button9 = Button(frame, text=9, command=lambda: Display_Number(9)).grid(row=3, column=2, sticky=N+S+E+W)

button4 = Button(frame, text=4, command=lambda: Display_Number(4)).grid(row=4, column=0, sticky=N+S+E+W)
button5 = Button(frame, text=5, command=lambda: Display_Number(5)).grid(row=4, column=1, sticky=N+S+E+W)
button6 = Button(frame, text=6, command=lambda: Display_Number(6)).grid(row=4, column=2, sticky=N+S+E+W)

button1 = Button(frame, text=1, command=lambda: Display_Number(1)).grid(row=5, column=0, sticky=N+S+E+W)
button2 = Button(frame, text=2, command=lambda: Display_Number(2)).grid(row=5, column=1, sticky=N+S+E+W)
button3 = Button(frame, text=3, command=lambda: Display_Number(3)).grid(row=5, column=2, sticky=N+S+E+W)

decimal_button = Button(frame, text=".", command=lambda: Display_Number(1)).grid(row=6, column=0, sticky=N+S+E+W)
button0 = Button(frame, text=0, command=lambda: Display_Number(0)).grid(row=6, column=1, sticky=N+S+E+W)
clear_button = Button(frame, text="CLEAR", command=lambda: Clear_Entry).grid(row=6, column=2, sticky=N+S+E+W)

for x in range(3):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(7):
  Grid.rowconfigure(frame, y, weight=1)

root.mainloop()