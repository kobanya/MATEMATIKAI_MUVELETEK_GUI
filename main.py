import tkinter as tk

def calculate_sum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    osszeg = num1 + num2
    kulonbseg = num1 - num2
    label1_result.config(text=f"A két szám összege: {osszeg}")
    label2_result.config(text=f"A két szám különbsége: {kulonbseg}")

root = tk.Tk()
root.title("SZÁMOLÁS")
root.geometry("400x300")

label1 = tk.Label(root, text="Első szám:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Második szám:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(root, text="Számol", command=calculate_sum)
button.grid(row=2, column=1, pady=20)

empty_label = tk.Label(root, text="", height=2)
empty_label.grid(row=3, column=0, columnspan=2)

label1_result = tk.Label(root, text="")
label1_result.grid(row=4, column=0, padx=10)

label2_result = tk.Label(root, text="")
label2_result.grid(row=5, column=0, padx=10)

root.mainloop()
