import src.visualization
import numpy as np
print(dir(src.visualization))
from .simulation import run_simulation
from .visualization import plot_results, animate_bar
from .control import zero_control, sinus_control, PID

if __name__ == "__main__":
    params = {"I": 1e-3, "k": 1e-1, "c": 2e-3}

    # Oscillation libre
    t, y = run_simulation(
    params,
    control_func=zero_control,
    t_max=5,
    y0=[np.pi, 0]   # départ à 180°
    )
    plot_results(t, y, title="Oscillation libre")
    animate_bar(t, y[0], title="Oscillation libre")

    # Battement forcé
    t, y = run_simulation(
    params,
    control_func=lambda t, s: sinus_control(t, s, amp=1e-2, freq=2),
    t_max=5,
    y0=[0, 0]
    )
    plot_results(t, y, title="Battement forcé")
    animate_bar(t, y[0], title="Battement forcé")

    # PID control
    pid = PID(Kp=1.0, Ki=0.1, Kd=0.05, target=0.0)
    t, y = run_simulation(
    params,
    control_func=pid,
    t_max=5,
    y0=[np.pi, 0]
    )
    plot_results(t, y, title="PID vers 0 rad")
    animate_bar(t, y[0], title="PID vers 0 rad")