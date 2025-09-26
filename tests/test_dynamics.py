from src.dynamics import dynamics
from src.control import zero_control

def test_dynamics_shape():
    params = {"I": 1e-6, "k": 1e-4, "c": 5e-5}
    state = [0.1, 0.0]
    result = dynamics(0.0, state, params, zero_control)
    assert len(result) == 2  # [dtheta, domega]
