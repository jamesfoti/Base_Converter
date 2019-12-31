from tkinter import *

# Create & Configure root
root = Tk()
root.title("Base Converter")
root.geometry("350x500")
root.configure(background = 'grey')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Title
title_label = Label(root, text = "Base Converter")
title_label.place(relwidth = 0.5, relheight = 0.1, relx = 0.05, rely = 0.05)

# Input field
number_label = Label(root, text = "Number: ")
number_label.place(relwidth = 0.25, relheight = 0.05, relx = 0.05, rely = 0.225)
entry1 = Entry(root)
entry1.place(relwidth = 0.5, relheight = 0.1, relx = 0.35, rely = 0.2)

# Dropdown menu for "from-base"
from_base_label = Label(root, text = "From base: ") # from-base label
from_base_label.place(relwidth = 0.25, relheight = 0.05, relx = 0.05, rely = 0.375)

OPTIONS = ["Binary", "Decimal", "Hexadecimal"] #etc
var = StringVar(root)
var.set(OPTIONS[1])

dropdown1 = OptionMenu(root, var, *OPTIONS)
dropdown1.place(relwidth = 0.5, relheight = 0.1, relx = 0.35, rely = 0.35)

# Dropdown menu for "to-base"
to_base_label = Label(root, text = "To base: ") # from-base label
to_base_label.place(relwidth = 0.25, relheight = 0.05, relx = 0.05, rely = 0.525)

var2 = StringVar(root)
var2.set(OPTIONS[1])

dropdown2 = OptionMenu(root, var2, *OPTIONS)
dropdown2.place(relwidth = 0.5, relheight = 0.1, relx = 0.35, rely = 0.50)

# Buttons
convert_button = Button(root, text = "Convert")
convert_button.place(relwidth = 0.25, relheight = 0.1, relx = 0.05, rely = 0.65)

clear_button = Button(root, text = "Clear")
clear_button.place(relwidth = 0.25, relheight = 0.1, relx = 0.35, rely = 0.65)

swap_button = Button(root, text = "Swap")
swap_button.place(relwidth = 0.25, relheight = 0.1, relx = 0.65, rely = 0.65)

# Result
result = Text(root)
result.insert(END, "TEST")
result.config(state=DISABLED)
result.place(relwidth = 0.5, relheight = 0.1, relx = 0.35, rely = 0.8)


root.mainloop()