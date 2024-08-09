import matplotlib.pyplot as plt
from odes import *
import os
import csv
from scipy.integrate import solve_ivp
import numpy as np
from tkinter import filedialog


def get_folder_path(path_var):
    path_var.set(filedialog.askdirectory())

    return path_var


def run_model(flist_dir, findex):
    flist = os.listdir(flist_dir)
    fpath = os.path.join(flist_dir,flist[findex])
    cumulative_time, wake_state = get_data(fpath)
    y0 = np.array([3.8, 38, 0.0212, 4])

    y_final = y0
    t_final = cumulative_time[0]
    #theta = [0.22, 0.037, 0.26, 0.0126, 22.02, 0.82, 1.5, 0.49, 21.2, 1.09, 1, 1.37, 0.71, 1.31] KSS
    theta = [0.028, 0.26, 0.26, 0.0126, 20.22, 0.466, 1.5, 0.49, 21.2, 1.09, 0, 1.37, 0.71, 1.31]  # PVT
    for time_start, time_end, sleepwake in zip(cumulative_time, cumulative_time[1:], wake_state):

        if sleepwake:
            fun = wakeode
        else:
            fun = sleepode

        result = solve_ivp(fun, [time_start, time_end], y0, method="RK45", t_eval=None, dense_output=True,
                           events=None, vectorized=False, args=(theta,), max_step=0.1, rtol=10 ** -8, atol=10 ** -8)
        y_final = np.c_[y_final, result.y[:, 1:]]
        t_final = np.r_[t_final, result.t[1:]]
        y0 = y_final[:, -1]

    plt.plot(t_final, y_final[0, :])
    plt.show()

    return y_final, t_final


def get_data(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        data = [{h: x for (h, x) in zip(headers, row)} for row in reader]

    # t_start = data[00].get("tib_time")
    time_list = [d['prot_time'] for d in data]
    all_time = [eval(i) for i in time_list]
    all_time.insert(0, 7.5)

    state_list = [d['sleepwake'] for d in data]
    all_wake = [eval(i) for i in state_list]
    all_wake.insert(0, 1)

    return all_time, all_wake

