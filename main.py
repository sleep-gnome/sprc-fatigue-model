import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from utilities import *


def update():
    file_list = os.listdir(path_var.get())
    fcombo_box.configure(values=file_list)

root = tk.Tk()
root.grid()
root.quitButton = ttk.Button()

# initialize needed Variables
path_var = tk.StringVar()
#file_list = []
#file_list.set('')

path_frame = tk.Frame(root, bg='lightpink', bd=20, width=900, height=600)
path_frame.grid()


fpath_label = tk.Label(path_frame, state=tk.DISABLED, textvariable=path_var, relief=tk.SUNKEN, width=64)
fpath_label.grid()
fcombo_box = ttk.Combobox(path_frame, values=[])
fpath_button = ttk.Button(path_frame, command=lambda: [get_folder_path(path_var), update()],
                          text="Find folder")
run_button = ttk.Button(path_frame, command=lambda: [run_model(path_var.get(), fcombo_box.current())], text="Run")

fpath_button.grid()
fcombo_box.grid()
run_button.grid()

root.mainloop()


#print(result.y)





