import matplotlib
matplotlib.use("Agg")  # backend non interactif pour les tests
from src.visualization import plot_results

def test_plot_results_runs_without_error():
    import numpy as np
    t = np.linspace(0, 0.1, 10)
    y = np.array([np.sin(t), np.cos(t)])
    # on vérifie juste que ça ne plante pas
    plot_results(t, y, title="test")
