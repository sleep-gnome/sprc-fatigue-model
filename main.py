import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from utilities import *
from tkinter import font

def update():
    file_list = os.listdir(path_var.get())
    fcombo_box.configure(values=file_list)

root = tk.Tk()
root.grid()
root.quitButton = ttk.Button()
root.geometry("1200x600")

#root.resizable(False, False)

# initialize needed Variables
path_var = tk.StringVar()

path_frame = tk.Frame(root, bg='honeydew', bd=0, width=1200, height=90)
path_frame.place(x=0, y=0)
plots_frame = tk.Frame(root, bg='lightgrey', bd=0, width=1110, height=450)
plots_frame.place(x=140, y=120)
left_frame = tk.Frame(root, bg='bisque', bd=0, width=130, height=450)
left_frame.place(x=0, y=120)
borderLeft_frame = tk.Frame(root, bg='darkseagreen', bd=0, width=10, height=450)
borderLeft_frame.place(x=130, y=120)
borderTop_frame = tk.Frame(root, bg='darkseagreen', bd=0, width=1200, height=40)
borderTop_frame.place(x=0, y=90)

s = ttk.Style()
s.configure(
    "MyButton.TButton",
    background='green', height= 5, width=10)
s2 = ttk.Style()
s2.configure(
    "MyButton2.TButton",
    background='yellow', height= 5, width=200)
fpath_pretext = tk.Label(path_frame, text=' Current Folder: ', bg='honeydew',font='bold')
fpath_pretext.place(x=110, y=0, width=110, height=30)


fpath_label = tk.Label(path_frame, state=tk.DISABLED, textvariable=path_var, width=80, height=1, bg='honeydew',
                       font='bold')
fpath_label.place(x=230, y=3)

fcombo_box = ttk.Combobox(path_frame, values=[], style="MyButton2.TButton")
fcombo_box.place(x=0,y=60)



dataType = []
with open('dataType.txt') as inFile:
    dataType = [line for line in inFile]

underlined_font = font.Font(family="Helvetica", size=13, underline=True)

plotOptions_label = tk.Label(left_frame, text='  Baseline Sleep   ', bg='tan', font='bold')
plotOptions_label.place(x=0, y=10)
plotOptions_label = tk.Label(left_frame, text='Length (h)', bg='bisque', font=['bold', 12])
plotOptions_label.place(x=0, y=42)
plotOptions_label = tk.Label(left_frame, text='WakeOnset', bg='bisque', font=('bold', 12))
plotOptions_label.place(x=0, y=72)



plotOptions_label = tk.Label(left_frame, text='  Plotting Options  ', bg='tan', font='bold')
plotOptions_label.place(x=0, y=100)

#def sel():
#   selection = "Sleep inertia is " + str(var.get())
   #selection = "Sleep inertia is " + str(var.get())
#   label.config(text = selection)
#root = Tk()
var = IntVar()
R1 = tk.Radiobutton(left_frame, text="Sleep Inertia", variable=var, value=1, bg='bisque', font='bold')
#R1 = tk.Radiobutton(left_frame, text="SI", variable=var, value=1, command=sel, bg='bisque', font='bold')
R1.place(x=0,y=130)
#R1.pack( anchor = W )
#R1.pack()
#R2 = tk.Radiobutton(left_frame, text="no SI", variable=var, value=0, bg='bisque', font='bold')
#R2 = tk.Radiobutton(left_frame, text="no SI", variable=var, value=0, command=sel, bg='bisque', font='bold')
#R2.place(x=60,y=120)
#R2.pack( anchor = W )
#R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
#R3.pack( anchor = W)
#label = Label(root)
#label.pack()

varPVTKSS = IntVar()
RPVT = tk.Radiobutton(left_frame, text="PVT", variable=varPVTKSS, value=1, bg='bisque', font='bold')
RPVT.place(x=0,y=160)
RKSS = tk.Radiobutton(left_frame, text="KSS", variable=varPVTKSS, value=0, bg='bisque', font='bold')
RKSS.place(x=60,y=160)

varData = IntVar()
R1data = tk.Radiobutton(left_frame, text="Plot Data", variable=varData, value=1, bg='bisque', font='bold')
#R1 = tk.Radiobutton(left_frame, text="SI", variable=var, value=1, command=sel, bg='bisque', font='bold')
R1data.place(x=0,y=190)






# Create instance
#win = tk.Tk()

# Add a title
#win.title("Combo Test")

# want to bwe able to add a new list of data column names. However, use the same names as the code will be looking for
# certain names to run the functions
# Creature Drop Down
#ttk.Label(path_frame, text="Select Creature").grid(column=1, row=1)
#creature_box = tk.StringVar()
#dataType_chosen = ttk.Combobox(path_frame, height=1, width=40, state='readonly', style="MyButton2.TButton")

#method = StringVar(value='default')
#choosen = ttk.Combobox(root, width = 14, textvariable = method, )

nameT = StringVar(value='default')

fpath_pretextDataType = tk.Label(path_frame, text=' File Format: ', bg='honeydew',font='bold')
fpath_pretextDataType.place(x=0, y=30, width=90, height=30)

dataType_chosen = ttk.Combobox(path_frame, width=50, style="MyButton2.TButton", textvariable=nameT)
dataType_chosen['values'] = list(dataType) #  tuple, list, set, and dictionary,
#dataType_chosen.grid(column=2, row=3)
dataType_chosen.current(0)
dataType_chosen.place(x=160,y=30)


baseTime = StringVar(value='7:30')
baseSleep = StringVar(value='8')

baseSleep_var = ttk.Combobox(left_frame, width=15, style="MyButton2.TButton", textvariable=baseSleep)
baseSleep_var.place(x=90,y=40, width=40)
baseTime_var = ttk.Combobox(left_frame, width=15, style="MyButton2.TButton", textvariable=baseTime)
baseTime_var.place(x=90,y=70,width=40)








# read dataType.dat and fill the combobox so that you choose which format of data you will be reading
# should produce an error occur if you choose a type that is not like the dat file you are downloading

#fdatatype_box = ttk.Combobox(path_frame, values=[], style="MyButton2.TButton")
#fdatatype_box.place(x=0,y=60)

show_data_button = ttk.Button(borderTop_frame, command=lambda: [get_folder_path(path_var), update()],
                          text="Show Data File", style="MyButton.TButton")
show_data_button.place(x=140, y=5, width=120, height=30)

save_data_button = ttk.Button(borderTop_frame, command=lambda: [get_folder_path(path_var), update()],
                          text="Save Data File", style="MyButton.TButton")
save_data_button.place(x=260, y=5, width=120, height=30)

make_plot_button = ttk.Button(borderTop_frame, command=lambda: [run_model(path_var.get(), fcombo_box.current())], text="Make Plot", style="MyButton.TButton")
make_plot_button.place(x=380, y=5, width=80, height=30)

make_sleep_predictions_button = ttk.Button(borderTop_frame, command=lambda: [get_folder_path(path_var), update()],
                          text="Make Sleep Predictions", style="MyButton.TButton")
make_sleep_predictions_button.place(x=460, y=5, width=160, height=30)

print_button = ttk.Button(borderTop_frame, command=lambda: [get_folder_path(path_var), update()],
                          text="Print Plot", style="MyButton.TButton")
print_button.place(x=620, y=5, width=80, height=30)



fpath_pretextFolder = tk.Label(path_frame, text=' Folder: ', bg='honeydew',font='bold')
fpath_pretextFolder.place(x=0, y=0, width=60, height=30)

fpath_button = ttk.Button(path_frame, command=lambda: [get_folder_path(path_var), update()],
                          text="Set", style="MyButton.TButton")

fpath_button.place(x=60, y=0, width=40, height=30)



#fpath_label.place(x=200,y=100)

# Creating a Button


quit_button = ttk.Button(path_frame, text='Quit', command=root.destroy, style="MyButton.TButton")

quit_button.place(x=1110, y=0, width=90,height=30)

#quit_button.grid()
#fpath_button.grid()
#fcombo_box.grid()
#run_button.grid()

root.mainloop()

#print(result.y)


# 1) Ability to load and display an airline trip (pairing) from a FedEx file (ask Mark or Rachael for examples)

# 2) Ability to invoke the new algorithm (Mark's version) to predict sleep for the schedule loaded in step 1 and
#       display the predicted sleep

# 3) Ability to invoke the 2024 model (Frontiers version) to predict fatigue (both PVT and KSS) for the schedule loaded
#       in step 1 with the sleep predicted in step 2

# 4) Ability to load and display actual sleep observations from actigraphy (ask Rachael about format)

# 5) Ability to invoke the 2024 model (Frontiers version*) to predict fatigue (both PVT and KSS) for the schedule
#       loaded in step 1 with the actual sleep loaded in step 4 *Later: recalibrate the 2024 model with actual sleep
#       (instead of time in bed) to make it truly valid for this purpose

# 6) Ability to load and display actual fatigue observations (PVT and/or KSS); file format to be determined

# 7) Ability to compare predicted sleep from step 2 to actual sleep from step 4

# 8) Ability to compare predicted fatigue from step 3 or from step 5 to actual fatigue (PVT and/or KSS) from step 6

# 9) Ability to compare sleep predictions from step 2 and fatigue predictions from step 3 between two different
#       schedules loaded in step 1

# 10) Implement a version of the 2024 model expanded with circadian resynchronization; then use step 9 to explore
#       the expanded model






