function

for time_start, time_end, sleepwake in zip(cumulative_time,cumulative_time[1:],wake_state):

    if sleepwake:
        fun = wakeode
    else:
        fun = sleepode

    result = solve_ivp(fun, [time_start, time_end], y0, method="RK45", t_eval=None, dense_output=True, events=None, vectorized=False,
                           args=(theta,), max_step=0.1, rtol=10 ** -8, atol=10 ** -8)
    yfinal = np.c_[yfinal, result.y[:,1:]]
    tfinal = np.r_[tfinal,result.t[1:]]
    y0 = yfinal[:,-1]