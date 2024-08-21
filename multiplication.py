from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Math table generator")
window.geometry("350x600")


choice_frame = Frame(window)

title = Label(choice_frame, text = "Mathematical Tabel", font = ("times", 43)).place(x = 0, y = 0)
choice_question = Label(choice_frame, text = "Number and Range: ", font = ("helvetica", 15)).grid(row = 1, column = 1, pady = 100, padx = 10)
generate = Button(choice_frame, text = "Generate").grid(row = 1, column = 3, padx = 10)

#creating combobox widjet
num = IntVar()
numbers = Combobox(choice_frame, textvariable = num, width = 5)
numbers["values"] = tuple(range(25))
numbers.grid(row = 1, column = 2)

choice_frame.grid(row = 1, column = 1)


result_frame = Frame(window)
result_frame.grid(row = 2, column = 1)

window.mainloop()