import tkinter

# Window
window = tkinter.Tk()
window.minsize(width=150, height = 100)
window.config(padx=10)
window.title("Converter")

# Label
TITLE_STYLE = ("Arial", 10, "normal")
NORMAL_STYLE = ("Arial", 10, "normal")

label = tkinter.Label(text = "Converter Application", font = TITLE_STYLE)
label.grid(column= 1, row = 0)

# Entry
miles = tkinter.Entry(font=NORMAL_STYLE, width=10)
miles.grid(column=1, row = 1)

# Label
miles_text = tkinter.Label(text = "Miles", font = NORMAL_STYLE)
miles_text.grid(column= 2, row = 1)

# Label
km_value = tkinter.Label(text = "0", font = NORMAL_STYLE)
km_value.grid(column = 1, row = 2)

# Label
km_text = tkinter.Label(text = "KM", font = NORMAL_STYLE)
km_text.grid(column = 2, row = 2)

# Label
equal_text = tkinter.Label(text = "is equal to", font = NORMAL_STYLE)
equal_text.grid(column = 0, row = 2)

# Button
def calculate():
    try:
        number_of_miles = int(miles.get())
        km_value.config(text = number_of_miles * 1.60934)
    except ValueError:
        pass


calculate_button = tkinter.Button(text = "Calculate", font = NORMAL_STYLE, command= calculate)
calculate_button.grid(column = 1, row = 3)

window.mainloop()