import math
from src.control import zero_control, sinus_control, PID

def test_zero_control():
    assert zero_control(0, [0, 0]) == 0.0

def test_sinus_control_range():
    u = sinus_control(0.0, [0, 0], amp=1.0, freq=1.0)
    assert abs(u) <= 1.0  # toujours borné par l’amplitude

def test_pid_outputs_float():
    pid = PID(1.0, 0.0, 0.0, target=1.0)
    u = pid(0.1, [0.0, 0.0])
    assert isinstance(u, float)
