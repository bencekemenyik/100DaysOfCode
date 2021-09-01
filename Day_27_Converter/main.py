import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=100)
window.title("Mile to Km Converter")

def calculate():
    result_label["text"] = round(int(input_entry.get()) * 1.609344, 1)

input_entry = tkinter.Entry()
input_entry.grid(column=1, row=0)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)

label2 = tkinter.Button(text="Calculate", command=calculate)
label2.grid(column=1, row=2)












window.mainloop()
