import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from odes import *

#yfinal = [None] * 3
#tfinal = [None]
tspan = np.array([7.5, 23.5])
y0 = np.array([3.8, 38, 0.0212])
yfinal = y0
tfinal = tspan[0]
theta = [0.028, 0.26, 0.26, 0.0074, 20.22, 0.33, 1.5, 0.49, 21.2, 1.09]
result = solve_ivp(wakeode, tspan, y0, method="RK45", t_eval=None, dense_output=True, events=None, vectorized=False,
                   args=(theta,),max_step=0.1, rtol=10**-8, atol=10**-8)
yfinal = np.c_[yfinal, result.y[:,1:]]
tfinal = np.r_[tfinal,result.t[1:]]
tspan = [23.5, 31.5]
print(result.y)
y0 = result.y[:,-1]
result = solve_ivp(sleepode, tspan, y0, method="RK45", t_eval=None, dense_output=True, events=None, vectorized=False,
                   args=(theta,),max_step=0.1, rtol=10**-8, atol=10**-8)

yfinal = np.c_[yfinal, result.y[:,1:]]
tfinal = np.r_[tfinal,result.t[1:]]
#print(result.y)

plt.plot(tfinal,yfinal[0,:])
plt.show()