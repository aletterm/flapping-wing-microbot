"""
simulate.py
Simulation simplifiée d’un micro-robot à ailes battantes
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# -----------------------------
# 1. Modèle dynamique
# -----------------------------
def dynamics(t, state, params, control_func):
    """
    Équations du mouvement.
    
    state : [theta, omega]
    params : dict avec I, k, c
    control_func : fonction u(t, state) qui renvoie le couple moteur
    """
    theta, omega = state
    I, k, c = params["I"], params["k"], params["c"]

    # couple moteur (externe)
    u = control_func(t, state)

    # équations différentielles
    dtheta = omega
    domega = (-k * theta - c * omega + u) / I

    return [dtheta, domega]


# -----------------------------
# 2. Fonctions de contrôle
# -----------------------------
def zero_control(t, state):
    """Pas de couple moteur (libre)."""
    return 0.0


def sinus_control(t, state, amp=1e-6, freq=20.0):
    """Couple moteur sinusoïdal pour forcer un battement."""
    return amp * np.sin(2 * np.pi * freq * t)


# -----------------------------
# 3. Simulation
# -----------------------------
def run_simulation(params, control_func=zero_control, t_max=0.1):
    """
    Lance la simulation et renvoie le temps et les états.
    """
    t_span = (0, t_max)
    y0 = [0.1, 0.0]  # condition initiale: petit angle, pas de vitesse

    sol = solve_ivp(
        dynamics, t_span, y0,
        args=(params, control_func),
        dense_output=True, max_step=1e-4
    )

    # échantillonnage uniforme pour faciliter le plotting
    t = np.linspace(t_span[0], t_span[1], 2000)
    y = sol.sol(t)
    return t, y


# -----------------------------
# 4. Visualisation
# -----------------------------
def plot_results(t, y, title="Résultats simulation"):
    theta, omega = y
    plt.figure(figsize=(8, 4))
    plt.plot(t, theta, label="θ (angle)")
    plt.plot(t, omega, label="ω (vitesse)")
    plt.xlabel("Temps (s)")
    plt.ylabel("Valeurs")
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()


# -----------------------------
# 5. Main
# -----------------------------
if __name__ == "__main__":
    # paramètres physiques (valeurs fictives mais plausibles)
    params = {
        "I": 1e-6,   # inertie
        "k": 1e-4,   # raideur ressort
        "c": 5e-5    # frottement
    }

    # Simulation sans contrôle
    t, y = run_simulation(params, control_func=zero_control, t_max=0.05)
    plot_results(t, y, title="Oscillation libre (sans contrôle)")

    # Simulation avec un sinus moteur
    t, y = run_simulation(
        params,
        control_func=lambda t, state: sinus_control(t, state, amp=5e-5, freq=10),
        t_max=0.5
    )
    plot_results(t, y, title="Battement forcé (sinusoidal)")
