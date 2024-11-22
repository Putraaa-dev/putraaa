import tkinter as tk
from tkinter import ttk

class ParkingApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Aplikasi Parkir")
        tk.Label(root, text="Cari NoPol").grid(row=0, column=0)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=0, column=1)
        tk.Button(root, text="Cari", command=self.search).grid(row=0, column=2)

        tk.Label(root, text="No Plat Polisi").grid(row=1, column=0)
        self.plate_entry = tk.Entry(root)
        self.plate_entry.grid(row=1, column=1)

        tk.Label(root, text="Waktu Masuk").grid(row=2, column=0)
        self.entry_time_entry = tk.Entry(root)
        self.entry_time_entry.grid(row=2, column=1)

        tk.Label(root, text="Waktu Keluar").grid(row=3, column=0)
        self.exit_time_entry = tk.Entry(root)
        self.exit_time_entry.grid(row=3, column=1)

        tk.Label(root, text="Biaya").grid(row=4, column=0)
        self.fee_entry = tk.Entry(root)
        self.fee_entry.grid(row=4, column=1)
        self.fee_entry.insert(0, "0")

        tk.Button(root, text="Submit", command=self.submit).grid(row=5, column=1)

        tk.Label(root, text="Biaya Per Jam", font=("Arial", 16)).grid(row=0, column=3, rowspan=2)
        tk.Label(root, text="Rp. 2.000", font=("Arial", 16)).grid(row=2, column=3, rowspan=2)

        # Listboxes
        tk.Label(root, text="List Pelanggan Urut Terakhir Keluar").grid(row=6, column=0, columnspan=2)
        self.recent_listbox = tk.Listbox(root)
        self.recent_listbox.grid(row=7, column=0, columnspan=2)

        tk.Label(root, text="List Pelanggan Banyak Bayar").grid(row=6, column=2, columnspan=2)
        self.top_payers_listbox = tk.Listbox(root)
        self.top_payers_listbox.grid(row=7, column=2, columnspan=2)

    def search(self):
        # Implement search functionality
        pass

    def submit(self):
        # Implement submit functionality
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingApp(root)
    root.mainloop()
