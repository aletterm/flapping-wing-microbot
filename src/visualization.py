import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plot_results(t, y, title="Résultats", target=None):
    theta, omega = y
    plt.figure(figsize=(8, 4))
    plt.plot(t, theta, label="θ (angle)")
    plt.plot(t, omega, label="ω (vitesse)")
    if target is not None:
        plt.axhline(target, color="r", linestyle="--", label="Consigne θ")
    plt.xlabel("Temps (s)")
    plt.ylabel("Valeurs")
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()

def animate_bar(time, theta, title="Animation"):
    """
    Animate a rotating bar based on the simulation angle.
    
    Parameters
    ----------
    time : array-like
        Time values from the simulation
    theta : array-like
        Angle values (radians) from the simulation
    title : str
        Title of the animation
    """
    fig, ax = plt.subplots()
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
    ax.set_title(title)

    # bar (line from origin to cos,sin)
    bar, = ax.plot([], [], lw=3)

    def init():
        bar.set_data([], [])
        return bar,

    def update(frame):
        x = [0, np.cos(theta[frame])]
        y = [0, np.sin(theta[frame])]
        bar.set_data(x, y)
        return bar,

    ani = animation.FuncAnimation(
        fig, update, frames=len(time), init_func=init,
        blit=True, interval=50, repeat=False
    )

    plt.show()
    return ani