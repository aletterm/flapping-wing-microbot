import numpy as np
from scipy.integrate import solve_ivp
from .dynamics import dynamics

def run_simulation(params, control_func, t_max=0.1):
    t_span = (0, t_max)
    y0 = [0.1, 0.0]
    sol = solve_ivp(
        dynamics, t_span, y0,
        args=(params, control_func),
        dense_output=True, max_step=1e-4
    )
    t = np.linspace(t_span[0], t_span[1], 2000)
    y = sol.sol(t)
    return t, y
