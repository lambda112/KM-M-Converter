import tkinter 

window = tkinter.Tk() # Create Window
window.title("Converter")
window.minsize(width=500, height=300)

#Label: 
my_label = tkinter.Label(text = "I am a label", font=("Arial", 24, "bold"))
my_label.pack() # Center on screen

my_label["text"] = "New Text" # Update Values
my_label.config(text = "New Text") # Update Values


# Button:
def button_clicked():
    my_label["text"] = "I Got Clicked"

button = tkinter.Button(text = "Click Me", command=button_clicked)
button.pack()


# Entry 
new_text = tkinter.Entry(width= 10)
new_text.pack()

def change_text():
    my_label["text"] = new_text.get()

button.config(command=change_text)


# Text
text = tkinter.Text(height=1, width=10)
text.focus() # Cursor is in the text box by default
text.insert(index = tkinter.END, chars = "Example!")
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_ = 0, to=10, width = 10, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)
    
scale = tkinter.Scale(from_ = 0, to = 100, command=scale_used)
scale.pack()


# Checkbox
def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar() # Variable to held check state, 0 off | 1 on
check_button= tkinter.Checkbutton(text = "Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
check_button.pack()


# Radio Button
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar() # Check which button is pressed
radio_button1 = tkinter.Radiobutton(text = "Option 1", value = 1, variable=radio_state, command=radio_used)
radio_button2 = tkinter.Radiobutton(text = "Option 1", value = 2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()


# Listbox
def list_box_used(event):
    print(list_box.get(list_box.curselection()))

list_box = tkinter.Listbox(height = 4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
[list_box.insert(fruits.index(item),item) for item in fruits]
list_box.bind(sequence = "<<ListboxSelect>>", func = list_box_used)
list_box.pack()


FONT_STYLE = ("Arial", 14, "normal")

# Setup Screen with Mainloop
window = tkinter.Tk()
window.title("Converter")
window.minsize(height = 300, width = 500)
window.config(padx=100, pady=100) # Add Padding

# Label - Displays Text
label = tkinter.Label(text="Example", font=FONT_STYLE)
label.grid(column = 0, row = 0)

# Button 
button1 = tkinter.Button(text = "Press Me", font = FONT_STYLE)
button1.grid(column = 1, row = 1)

# Button 
button2 = tkinter.Button(text = "Press Me", font = FONT_STYLE)
button2.grid(column = 2, row = 0)

# Entry
entry = tkinter.Entry()
entry.grid(column= 3, row = 3)

window.mainloop() # Keep Window Open End of Program
