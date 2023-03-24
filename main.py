'''
NB-2023.03.22
Különböző műveletek, grafikus felülettel

'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ---------------- MŰVELETEK ---------------------------------------------

def szamolas():
    try:
        szam1 = int(entry1.get())
        szam2 = int(entry2.get())
        result = szam1 + szam2     # ellenőrzi, hogy csak számot adtál-e meg

    except ValueError:
        messagebox.showerror("Hiba", "Kérem, csak számot adjon meg!")

    if szam1 == 0:                  # ellenőrzi, hogy az egyik szám nem  nulla-e
        messagebox.showerror("Hiba", "A megadott szám nem lehet 0, mivel nullával nem lehet osztani!")
        return

    if szam2 == 0:
        messagebox.showerror("Hiba", "A megadott szám nem lehet 0, mivel nullával nem lehet osztani!")
        return

    szam1 = int(entry1.get())
    szam2 = int(entry2.get())
    osszeg = szam1 + szam2
    kulonbseg = szam1 - szam2
    szorzat = szam1 * szam2
    hanyados = szam1 / szam2
    atlag= (szam1+szam2) /2

    if szam1 % 2 == 0:
        label5_result.config(text=f"Az első szám, ami {szam1} - PÁROS")
    else:
        label5_result.config(text=f"Az első szám, ami {szam1} - PÁRATLAN")

    if szam2 % 2 == 0:
        label6_result.config(text=f"A második szám, ami {szam2} - PÁROS")
    else:
        label6_result.config(text=f"A masodik szám, ami {szam2} - PÁRATLAN")

    label1_result.config(text=f"A két szám összege: {osszeg}")
    label2_result.config(text=f"A két szám különbsége: {kulonbseg}")
    label3_result.config(text=f"A két szám szorzata: {szorzat}")
    label4_result.config(text=f"A két szám hányadosa: {hanyados:.2f}")
    label7_result.config(text=f"A két szám atlaga: {atlag:.2f}")

#---------------------------------- TÖRLÉS ---------------------------------
def  torles():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label1_result.config(text=f"A két szám összege: 0 ")
    label2_result.config(text=f"A két szám különbsége: 0")
    label3_result.config(text=f"A két szám szorzata: 0")
    label4_result.config(text=f"A két szám hányadosa: 0")
    label7_result.config(text=f"A két szám atlaga: 0")
    label5_result.config(text=f"Az első szám,  -")
    label6_result.config(text=f"A második szám, -")

#-------------------------------------------- G U I  ------------------------

root = tk.Tk()
root.title("SZÁMOLÁS")
root.geometry("450x550")

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

button = tk.Button(root, text="Számol", command=szamolas)
button.grid(row=3, column=1, pady=20)

button = tk.Button(root, text="Töröl", command=torles)
button.grid(row=3, column=0, pady=20)

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

label5_result = tk.Label(root, text="")
label5_result.grid(row=11, column=0, padx=10, pady=5, sticky="w")

label6_result = tk.Label(root, text="")
label6_result.grid(row=12, column=0, padx=10, pady=5, sticky="w")

label7_result = tk.Label(root, text="")
label7_result.grid(row=13, column=0, padx=10, pady=5, sticky="w")

empty_label = tk.Label(root, text=" ", height=5)
empty_label.grid(row=14, column=0, columnspan=2)

root.mainloop()
