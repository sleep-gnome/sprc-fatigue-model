import matplotlib.pyplot as plt
import csv
import tkinter as tk
from utilities import *




root = tk.Tk()
root.grid()
root.quitButton = tk.Button()

path_frame = tk.Frame(root, bg='lightpink', bd=20, width=900, height=600)
path_frame.grid()

path_var = tk.StringVar()
fpath_label = tk.Label(path_frame, state=tk.DISABLED, textvariable=path_var, relief=tk.SUNKEN, width=64)
fpath_label.grid()

fpath_button = tk.Button(path_frame, command=get_folder_path(path_var),text="Find folder")
fpath_button.grid()
#root.withdraw()

root.mainloop()



with open(file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)
    data = [{h: x for (h, x) in zip(headers, row)} for row in reader]

#t_start = data[00].get("tib_time")

#
time_list = [d['prot_time'] for d in data]
all_time = [eval(i) for i in time_list]
all_time.insert(0, 7.5)

state_list = [d['sleepwake'] for d in data]
all_wake = [eval(i) for i in state_list]
all_wake.insert(0, 1)
#wake_state = bool(state_list)


#tspan = np.array([7.5, 23.5])
y0 = np.array([3.8, 38, 0.0212])


yfinal, tfinal = run_model(all_time, all_wake)

#print(result.y)

plt.plot(tfinal, yfinal[0, :])
plt.show()



