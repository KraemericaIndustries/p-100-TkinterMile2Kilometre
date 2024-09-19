from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=10, pady=10)

def button_clicked():
    miles = int(value.get())
    km = str(miles * 1.609)
    result_label.config(text=km)

#Entry
value = Entry(width=10)
value.insert(END, string="0")
value.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

#Label
equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

#Label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

#Label
result_label = Label(text="0", font=("Arial", 12, "bold"))
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()