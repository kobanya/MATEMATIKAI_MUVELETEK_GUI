import tkinter as tk
from tkinter import ttk

def calculate_sum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    osszeg = num1 + num2
    kulonbseg = num1 - num2
    szorzat = num1 * num2
    hanyados = num1 / num2
    label1_result.config(text=f"A két szám összege: {osszeg}")
    label2_result.config(text=f"A két szám különbsége: {kulonbseg}")
    label3_result.config(text=f"A két szám szorzata: {szorzat}")
    label4_result.config(text=f"A két szám hányadosa: {hanyados:.2f}")

#-------------------------------------------- G U I  ------------------------

root = tk.Tk()
root.title("SZÁMOLÁS")
root.geometry("500x400")

label_intro = tk.Label(root, text="Kérlek írj be két számot, majd nyomd meg a SZÁMOL gombot:")
label_intro.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


label1 = tk.Label(root, text="Első szám:")
label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry1 = tk.Entry(root, width=10)
entry1.grid(row=1, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Második szám:")
label2.grid(row=2, column=0, padx=5, pady=5, sticky="w")

entry2 = tk.Entry(root, width=10)
entry2.grid(row=2, column=1, padx=5, pady=5)

button = tk.Button(root, text="Számol", command=calculate_sum)
button.grid(row=3, column=1, pady=20)

empty_label = tk.Label(root, text="", height=2)
empty_label.grid(row=4, column=0, columnspan=2)

separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=5, columnspan=2, sticky="ew", padx=10, pady=10)

label1_result = tk.Label(root, text="")
label1_result.grid(row=6, column=0, padx=10, pady=5, sticky="w")

label2_result = tk.Label(root, text="")
label2_result.grid(row=7, column=0, padx=10, pady=5, sticky="w")

label3_result = tk.Label(root, text="")
label3_result.grid(row=8, column=0, padx=10, pady=5, sticky="w")

label4_result = tk.Label(root, text="")
label4_result.grid(row=9, column=0, padx=10, pady=5, sticky="w")


separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=10, columnspan=2, sticky="ew", padx=10, pady=10)


empty_label = tk.Label(root, text="", height=5)
empty_label.grid(row=13, column=0, columnspan=2)

root.mainloop()
