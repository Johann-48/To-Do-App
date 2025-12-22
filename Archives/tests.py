import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.geometry("300x200")

date_picker = DateEntry(root, date_pattern="dd/mm/yyyy")
date_picker.pack(pady=20)

root.mainloop()
