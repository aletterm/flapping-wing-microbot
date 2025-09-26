import matplotlib.pyplot as plt

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

