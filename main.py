import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from odes import *

fun = wakeode
tspan = [7.5, 23.5]
y0 = [3.8, 38, 0.0212]
theta = [0.028, 0.26, 0.26, 0.0074, 20.22, 0.33, 1.5, 0.49, 21.2, 1.09]
result = solve_ivp(fun, tspan, y0, method="RK45", t_eval=None, dense_output=True, events=None, vectorized=False,
                   args=(theta,),max_step=0.1, rtol=10**-8, atol=10**-8)

print(result)

plt.plot(result.t,result.y[0,:])
plt.show()