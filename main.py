from tkinter import *

BACKGROUND_COLOR = 'white'
FONT = ("Times New Roman", 12, "bold")

window = Tk()
window.title("Miles to km converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

# 1st label, indicates how much the number of inserted miles is equal to:
equal_to = Label(text="is equal to", font=FONT, bg=BACKGROUND_COLOR)
equal_to.grid(column=0, row=1)


def validate_entry(text):
    return text.isdecimal()


# Entry, where you put the amount of miles you would like to convert (only accepts numbers):
miles_input = Entry(bg="light blue", font=FONT, bd=2, justify='center', width=20, validate="key",
                    validatecommand=(window.register(validate_entry), "%S"))
miles_input.grid(column=1, row=0)

# def temp_text(event):
#     miles_input.delete(0, "end")


# function that will convert miles given to kilometers:
def convert_to_km():
    miles_to_convert = int(miles_input.get())
    converted_km = miles_to_convert * 1.609
    converted.config(text=converted_km)


# 2nd label, KM number of converted miles:
converted = Label(text='0', font=FONT, bg=BACKGROUND_COLOR)
converted.grid(column=1, row=1)

# Calculate button:
calculate = Button(text='calculate', font=FONT, bg=BACKGROUND_COLOR, command=convert_to_km)
calculate.grid(column=1, row=2)

# 3rd label, the miles title placed right next to the input box:
miles_label = Label(text="Miles", font=FONT, bg=BACKGROUND_COLOR)
miles_label.grid(column=2, row=0)

# 4th label, the kilometers label:
kilometers_label = Label(text='Km', font=FONT, bg=BACKGROUND_COLOR)
kilometers_label.grid(column=2, row=1)

window.mainloop()
