from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label =  Label(text="Miles", font=("Times new roman", 24, "bold"))
my_label.grid(row=0, column=2)

my_label_2 = Label(text="Km",font=("Times new roman", 24, "bold"))
my_label_2.grid(row=1, column=2)

my_label_3 = Label(text="is equal to",font=("Times new roman", 24, "bold"))
my_label_3.grid(row=1, column=0)

my_label_4 = Label(text="",font=("Times new roman", 24, "bold"))
my_label_4.grid(row=1, column=1)

def button_clicked():
    km = round(float(input.get()) * 1.609 ,2)
    return my_label_4.config(text=str(km))

button = Button(text="calculate", command=button_clicked)
button.grid(row=2, column=1)


input = Entry(width=10)
input.grid(row=0, column=1)


window.mainloop()