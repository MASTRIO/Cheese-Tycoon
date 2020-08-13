import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, 'What do you want to do?')
tk.mainloop()