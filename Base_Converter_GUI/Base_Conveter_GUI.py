"""
SOURCES!
https://www.rapidtables.com/convert/number/base-converter.html
https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
https://stackoverflow.com/questions/41416788/python-resizing-widgets-when-window-is-resized-using-place-manager
https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
https://stackoverflow.com/questions/30685308/how-do-i-change-the-text-size-in-a-label-widget-python-tkinter/30685801
https://stackoverflow.com/questions/42942534/how-to-change-the-color-of-a-tkinter-label-programmatically
https://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix
https://stackoverflow.com/questions/46495160/make-a-label-bold-tkinter/46495200
https://stackoverflow.com/questions/16046743/how-to-change-tkinter-button-state-from-disabled-to-normal
https://stackoverflow.com/questions/47378715/tkinter-how-to-get-the-value-of-an-entry-widget
https://www.daniweb.com/programming/software-development/code/487653/access-the-clipboard-via-tkinter
https://stackoverflow.com/questions/27913310/how-to-get-the-content-of-a-tkinter-text-object
"""

from tkinter import *
import numpy as np

# Create & Configure root
root = Tk()
root.title("Base Converter")
root.geometry("350x500")
root.resizable(0, 0)
root.configure(background='light grey')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Title
title_label = Label(root, text="BASE CONVERTER")
title_label.config(bg="light grey", font=("TkHeadingFont", 16, "bold"))
title_label.place(relwidth=0.565, relheight=0.1, relx=0.235, rely=0.03)

# Input field
number_label = Label(root, text="Number:")
number_label.config(bg="light grey", font=("TkSmallCaptionFont", 12, "bold"))
number_label.place(relwidth=0.25, relheight=0.05, relx=0.24, rely=0.155)
entry = Entry(root)
entry.config(font=("TkSmallCaptionFont", 14))
entry.place(relwidth=0.5, relheight=0.06, relx=0.265, rely=0.20)

# Options for both dropdown menus
OPTIONS = ["Binary", "Decimal", "Hexadecimal"]  # etc

# Dropdown menu for "from-base"
from_base_label = Label(root, text="From base: ")  # from-base label
from_base_label.config(bg="light grey", font=("TkSmallCaptionFont", 12, "bold"))
from_base_label.place(relwidth=0.26, relheight=0.05, relx=0.265, rely=0.30)
from_base_dropdown_value = StringVar(root)
from_base_dropdown_value.set(OPTIONS[1])
from_base_dropdown_menu = OptionMenu(root, from_base_dropdown_value, *OPTIONS)
from_base_dropdown_menu.config(bg="white", font=("TkSmallCaptionFont", 12))
from_base_dropdown_menu.place(relwidth=0.5, relheight=0.075, relx=0.265, rely=0.345)

# Dropdown menu for "to-base"
to_base_label = Label(root, text="To base: ")  # from-base label
to_base_label.config(bg="light grey", font=("TkSmallCaptionFont", 12, "bold"))
to_base_label.place(relwidth=0.25, relheight=0.05, relx=0.235, rely=0.455)
to_base_dropdown_value = StringVar(root)
to_base_dropdown_value.set(OPTIONS[1])  # DEFAULT value
to_base_dropdown_menu = OptionMenu(root, to_base_dropdown_value, *OPTIONS)
to_base_dropdown_menu.config(bg="white", font=("TkSmallCaptionFont", 12))
to_base_dropdown_menu.place(relwidth=0.5, relheight=0.075, relx=.265, rely=0.50)

# Buttons
convert_button = Button(root, text="Convert", command=lambda: convert())
convert_button.config(bg="white", font=("TkSmallCaptionFont", 12, "bold"))
convert_button.place(relwidth=0.25, relheight=0.1, relx=0.07, rely=0.64)

clear_button = Button(root, text="Clear", command=lambda: clear())
clear_button.config(bg="white", font=("TkSmallCaptionFont", 12, "bold"))
clear_button.place(relwidth=0.25, relheight=0.1, relx=0.37, rely=0.64)

swap_button = Button(root, text="Swap", command=lambda: swap())
swap_button.config(bg="white", font=("TkSmallCaptionFont", 12, "bold"))
swap_button.place(relwidth=0.25, relheight=0.1, relx=0.67, rely=0.64)

# Result
result = Text(root)
result.insert(END, "Result. . .")
result.config(font=("TkSmallCaptionFont", 12), state=DISABLED)
result.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.78)

# Copy to clipboard button
copy_button = Button(root, text="Copy", command=lambda: copy())
copy_button.config(bg="white", font=("TkSmallCaptionFont", 12, "bold"))
copy_button.place(relwidth=0.18, relheight=0.065, relx=0.25, rely=0.90)


def convert():
    print("Convert")

    # Re-enable text widget and clear its contents
    result.config(state=NORMAL)
    result.delete('1.0', END)

    if from_base_dropdown_value.get() == to_base_dropdown_value.get():
        result.insert(END, entry.get())

    # Insert the value and disable the text widget
    result.config(state=DISABLED)


def clear():
    print("Clear")
    entry.delete(0, END)
    result.config(state=NORMAL)
    result.delete('1.0', END)
    result.config(state=DISABLED)


def swap():
    print("Swap")
    temp = from_base_dropdown_value.get()
    from_base_dropdown_value.set(to_base_dropdown_value.get())
    to_base_dropdown_value.set(temp)


def copy():
    print("Copied")
    root.clipboard_clear()
    root.clipboard_append(result.get("1.0", "end-1c"))


# Decimal_To_Binary():
# Do stuff

# Decimal_To_Hex():
# Do stuff

# Binary_To_Decimal():
# Do stuff

# Binary_To_Hex():
# Do stuff

# Hex_To_Decimal():
# Do stuff

# Hex_To_Binary():
# Do stuff

root.mainloop()
