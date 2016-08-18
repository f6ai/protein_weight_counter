import tkinter
from tkinter import messagebox
import protein_weight_counter


def test():
    sequence = text.get("1.0", tkinter.END)
    protein_sum = 0
    for line in sequence.split("\n"):
        protein_sum += protein_weight_counter.count_weights(line.upper())
    v.set(protein_sum)
    ##messagebox.showinfo("Molecular Weight", protein_sum)

window = tkinter.Tk()
text = tkinter.Text(window)
text.pack()

but = tkinter.Button(window, text="Calculate", command=test)
but.pack()

v = tkinter.StringVar()

results = tkinter.Entry(window, textvariable=v)
results.pack()

text.focus_set()
window.mainloop()

