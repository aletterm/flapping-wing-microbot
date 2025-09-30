import numpy as np
from scipy.integrate import solve_ivp
from .dynamics import dynamics

def run_simulation(params, control_func, t_max=0.1, y0=None):
    """
    Run a simulation of the system dynamics.

    Parameters
    ----------
    params : dict
        System parameters (I, k, c).
    control_func : callable
        Control function u(t, state).
    t_max : float, optional
        Simulation duration (s).
    y0 : list or array-like, optional
        Initial conditions [theta, omega].
        Defaults to [0.1, 0.0].

    Returns
    -------
    t : ndarray
        Time array.
    y : ndarray
        State array [theta(t), omega(t)].
    """
    t_span = (0, t_max)

    # Default initial condition
    if y0 is None:
        y0 = [0.1, 0.0]

    sol = solve_ivp(
        dynamics,
        t_span,
        y0,
        args=(params, control_func),
        dense_output=True,
        max_step=1e-2
    )

    t = np.linspace(t_span[0], t_span[1], 100)
    y = sol.sol(t)
    return t, y
