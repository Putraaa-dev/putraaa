import tkinter as tk
from tkinter import ttk
def kalkulasi():
    Harga = float(Harga_entry.get())
    Kuantitas = float(Kuantitas_entry.get())
    Hitung = Harga * Kuantitas
    Kuantitas
    Hasil_label.config(text=f"Hasil: {Hitung:.2f}")

window = tk.Tk()
window.title("Program Kasir")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10)

Harga_label = ttk.Label(input_frame, text="Harga:")
Harga_label.grid(row=0, column=0, sticky="w")
Harga_entry = ttk.Entry(input_frame)
Harga_entry.grid(row=0, column=1)

Kuantitas_label = ttk.Label(input_frame, text="Kuantitas:")
Kuantitas_label.grid(row=1, column=0, sticky="w")
Kuantitas_entry= ttk.Entry(input_frame)
Kuantitas_entry.grid(row=1, column=1)

Kalkulasi_button = ttk.Button(window, text="Hitung", command=kalkulasi)
Kalkulasi_button.pack(pady=10)

Hasil_label = ttk.Label(window, text="")
Hasil_label.pack()

window.mainloop()