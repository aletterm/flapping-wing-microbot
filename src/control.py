import numpy as np

def zero_control(t, state):
    """Pas de couple moteur (libre)."""
    return 0.0

def sinus_control(t, state, amp=1e-6, freq=20.0):
    """Couple moteur sinusoïdal pour forcer un battement."""
    return amp * np.sin(2 * np.pi * freq * t)

class PID:
    """Contrôleur PID simple."""
    def __init__(self, Kp, Ki, Kd, target=0.0):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.target = target
        self.integral = 0.0
        self.prev_error = 0.0
        self.prev_time = None

    def __call__(self, t, state):
        theta, _ = state
        error = self.target - theta
        dt = 0 if self.prev_time is None else t - self.prev_time
        self.integral += error * dt
        derivative = 0.0 if dt == 0 else (error - self.prev_error) / dt
        u = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error, self.prev_time = error, t
        return u


if __name__ == "__main__":
    print("✅ Module control prêt")
