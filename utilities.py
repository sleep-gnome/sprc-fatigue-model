import tkinter

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from odes import *
from matplotlib.patches import Rectangle
import subprocess, os, platform
import csv
from scipy.integrate import solve_ivp
import numpy as np
from tkinter import filedialog
import matplotlib.colors as colors
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})


def get_folder_path(path_var):
    path_var.set(filedialog.askdirectory())


def open_data_file(flist_dir, findex):
    flist = os.listdir(flist_dir)
    file_path = os.path.join(flist_dir, flist[findex])
    if platform.system() == 'Darwin':           # macOS
        subprocess.call(('open', file_path))
    elif platform.system() == 'Windows':        # Windows
        os.startfile(file_path)
    else:                                       # linux variants
        subprocess.call(('xdg-open', file_path))


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list('trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def run_model(flist_dir, findex, plt_frame):
    flist = os.listdir(flist_dir)
    fpath = os.path.join(flist_dir,flist[findex])
    cumulative_time, wake_state = get_data(fpath)

    #theta = [0.22, 0.037, 0.26, 0.0126, 22.02, 0.82, 1.5, 0.49, 21.2, 1.09, 1, 1.37, 0.71, 1.31] KSS
    theta = [0.028, 0.26, 0.26, 0.0126, 20.22, 0.466, 1.5, 0.49, 21.2, 1.09, 0, 1.37, 0.71, 1.31]  # PVT
    y0 = np.array([3.8, 38, 0.0212, 4])

#print(R1.get())

# run a loop to get initial conditions
    for x in range(1, 10000):
       result = solve_ivp(wakeode, [7.5 + x * 24, 23.5 + x * 24], y0, method="RK45", t_eval=None, dense_output=True,
                           events=None, vectorized=False, args=(theta,), max_step=0.1, rtol=10 ** -8, atol=10 ** -8)
       resultW = np.c_[y0, result.y[:, 1:]]
       resultS = solve_ivp(sleepode, [23.5 + x * 24, 31.5 + x * 24], resultW[:, -1], method="RK45", t_eval=None, dense_output=True,
                           events=None, vectorized=False, args=(theta,), max_step=0.1, rtol=10 ** -8, atol=10 ** -8)
       result = np.c_[resultW[:,0:], resultS.y[:, 1:]]
       y1 = result[1,0] - result[1,-1]

       if (y1 < 0.00001):
          break

       y1 = result[1,0] - result[1,-1]
       y0 = result[:, -1]

    y_finalAll = y0
    t_finalAll = cumulative_time[0]
    y_thisPeriod = y0
    t_thisPeriod = cumulative_time[0]

#    tib_time,pvt
    plt_frame.update()
    px = 1 / plt.rcParams['figure.dpi']
    fr_w = plt_frame.winfo_width()
    fr_h = plt_frame.winfo_height()
    fig = plt.figure(figsize=(1, 1))


    for time_start, time_end, sleepwake in zip(cumulative_time, cumulative_time[1:], wake_state):
        if sleepwake:
            flag = 1
            fun = wakeode
        else:
            # print last wake concatenated list
            if flag == 1:
                flag = 0
                plt.plot(t_thisPeriod[0:], y_thisPeriod[0, 0:], color='black',linewidth=3)
                #plt.legend(loc='best')

            fun = sleepode

        result = solve_ivp(fun, [time_start, time_end], y0, method="RK45", t_eval=None, dense_output=True,
                           events=None, vectorized=False, args=(theta,), max_step=0.1, rtol=10 ** -8, atol=10 ** -8)
        y_finalAll = np.c_[y_finalAll, result.y[:, 1:]]
        t_finalAll = np.r_[t_finalAll, result.t[1:]]
        if sleepwake:
            y_thisPeriod = np.c_[y_thisPeriod, result.y[:, 1:]]
            t_thisPeriod = np.r_[t_thisPeriod, result.t[1:]]
        else:
            fig.set_size_inches(14, 6, forward=True)
            #cmap = plt.cm.get_cmap('jet')
            plt.gca().add_patch(Rectangle((result.t[0], 0), result.t[-1]-result.t[0], -2, fill=True, color='forestgreen', alpha=0.5, zorder=100, figure=fig))
            y_thisPeriod = result.y[:, -1]
            t_thisPeriod = result.t[-1]

        y0 = y_finalAll[:, -1]

    plt.gca().add_patch(Rectangle((t_finalAll[0], -2), t_finalAll[-1], 2, fill=True, color='whitesmoke',
                                  alpha=0.5, zorder=100, figure=fig))
    plt.gca().add_patch(Rectangle((t_finalAll[0], 0), t_finalAll[-1], 10, fill=True, color='lightgrey',
                                  alpha=0.5, zorder=100,figure=fig))
    plt.gca().add_patch(Rectangle((t_finalAll[0], 10), t_finalAll[-1], 10, fill=True, color='darkgrey',
                                  alpha=0.5, zorder=100, figure=fig))
    plt.gca().add_patch(Rectangle((t_finalAll[0], 20), t_finalAll[-1], 20, fill=True, color='grey',
                                  alpha=0.5, zorder=100, figure=fig))

    plt.xticks(np.arange(0, 500, step=24), labels=[str(i) for i in range(21)],fontsize=18)
    plt.yticks(np.arange(0, 35, step=5), labels=[str(i*5) for i in range(7)],fontsize=18)
    plt.xlim(t_finalAll[0], t_finalAll[-1])
    plt.ylim(-2, 30)
    plt.ylabel('PVT (lapses)', fontsize=20)
    plt.xlabel('Day', fontsize=20)
    plt.title(flist[findex], fontsize=20)

    plt_frame.update()
    #px =
    fig.set_size_inches((fr_w*0.01, 420*0.01))
    #fig.set_size_inches((3,3))
    plt.grid()
    # plt.show()

    canvas = FigureCanvasTkAgg(fig, master=plt_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, plt_frame)
    toolbar.update()
    canvas.get_tk_widget().pack()
    # canvas.draw()

    return y_finalAll, t_finalAll


def get_data(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
       # df = pd.read_csv('./file.csv', dtype='Int64')
        headers = next(reader)
        data = [{h: x for (h, x) in zip(headers, row)} for row in reader]

    # t_start = data[00].get("tib_time")
    time_list = [d['prot_time'] for d in data]
    pvt_list = [d['pvt'] for d in data]
    #pvt_list = pvt_list[~np.isnan(pvt_list)]
    #print(~np.isnan(pvt_list).any(axis=1))

    #pvt_list = [int(i) for i in ~isnan(pvt_list)]
    all_time = [eval(i) for i in time_list]
    #all_pvt = [eval(i) for i in pvt_list]
    #all_pvttime = all_time
    all_time.insert(0, 7.5)

    state_list = [d['sleepwake'] for d in data]
    all_wake = [eval(i) for i in state_list]
    all_wake.insert(0, 1)

    return all_time, all_wake

