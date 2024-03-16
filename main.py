import tkinter 

window = tkinter.Tk() # Create Window
window.title("Converter")
window.minsize(width=500, height=300)

#Label: 
my_label = tkinter.Label(text = "I am a label", font=("Arial", 24, "bold"))
my_label.pack(expand=True) # Center on screen





window.mainloop() # Keep Window Open End of Program
