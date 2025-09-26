import numpy as np

def dynamics(t, state, params, control_func):
    """Équations du mouvement [theta, omega]."""
    theta, omega = state
    I, k, c = params["I"], params["k"], params["c"]
    u = control_func(t, state)
    dtheta = omega
    domega = (-k * theta - c * omega + u) / I
    return [dtheta, domega]
