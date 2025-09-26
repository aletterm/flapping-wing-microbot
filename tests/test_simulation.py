import numpy as np
from src.simulation import run_simulation
from src.control import zero_control

def test_run_simulation_returns_arrays():
    params = {"I": 1e-6, "k": 1e-4, "c": 5e-5}
    t, y = run_simulation(params, control_func=zero_control, t_max=0.01)
    assert isinstance(t, np.ndarray)
    assert y.shape[0] == 2  # theta et omega
