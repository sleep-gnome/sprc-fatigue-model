from odes import *
from scipy.integrate import solve_ivp
import numpy as np
from tkinter import filedialog


def get_folder_path(path_var):
    path_var.set(filedialog.askdirectory())

    return path_var

def run_model(cumulative_time, wake_state,y0):
    y_final = y0
    t_final = cumulative_time[0]
    theta = [0.028, 0.26, 0.26, 0.0074, 20.22, 0.33, 1.5, 0.49, 21.2, 1.09]
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

    return y_final, t_final