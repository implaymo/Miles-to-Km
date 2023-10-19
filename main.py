from tkinter import *

# Window
window = Tk()
window.title("My first GUI program")
window.wm_minsize(100, 100)


def miles_to_km_conversion():
    """Converts Miles to Km"""
    conversion = int(input.get()) * 1.609344
    result_label.config(text=f"{round(conversion)}")


# Is equal to Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_to_label.grid(column=0, row=1)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=3, row=0)

# Km Label
km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=3, row=1)

# Conversion result label
result_label = Label(text="0", font=("Arial", 10, "bold"))
result_label.grid(column=1, row=1)


# Button to do the conversion
button = Button(text="Calculate", command=miles_to_km_conversion)
button.grid(column=1, row=3)

# Entry
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)









window.mainloop()