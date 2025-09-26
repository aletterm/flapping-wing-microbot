import src.visualization
print(dir(src.visualization))
from .simulation import run_simulation
from .visualization import plot_results
from .control import zero_control, sinus_control, PID

if __name__ == "__main__":
    params = {"I": 1e-6, "k": 1e-4, "c": 5e-5}

    t, y = run_simulation(params, control_func=zero_control, t_max=0.05)
    plot_results(t, y, title="Oscillation libre")

    t, y = run_simulation(
        params,
        control_func=lambda t, s: sinus_control(t, s, amp=5e-2, freq=10),
        t_max=0.5
    )
    plot_results(t, y, title="Battement forcé")

    pid = PID(Kp=2e-2, Ki=1e-6, Kd=2e-4, target=0.05)
    t, y = run_simulation(params, control_func=pid, t_max=0.5)
    plot_results(t, y, title="PID vers 0.05 rad", target=0.05)

