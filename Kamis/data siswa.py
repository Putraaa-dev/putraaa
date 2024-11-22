import tkinter as tk
from tkinter import messagebox


def save_data():
    messagebox.showinfo("Info", "Data saved successfully!")


def delete_data():
    entry_full_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_school.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_father_name.delete(0, tk.END)
    entry_mother_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(1.0, tk.END)


root = tk.Tk()
root.title("DATA SISWA BARU")


labels = ["Nama Lengkap", "Tanggal Lahir", "Asal Sekolah", "NISN", "Nama Ayah", "Nama Ibu", "Nomor Telepon / HP", "Alamat"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
    if label == "Alamat":
        entry = tk.Text(root, height=4, width=30)
    else:
        entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_full_name, entry_dob, entry_school, entry_nisn, entry_father_name, entry_mother_name, entry_phone, entry_address = entries


tk.Button(root, text="Hapus", command=delete_data).grid(row=len(labels), column=0, padx=10, pady=10)
tk.Button(root, text="Simpan", command=save_data).grid(row=len(labels), column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
