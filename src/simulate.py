import numpy as np
import matplotlib.pyplot as plt

# Simple wing oscillation demo
t = np.linspace(0, 2, 1000)          # 2 seconds, 1000 samples
x = np.sin(2 * np.pi * 5 * t)        # flapping at 5 Hz

plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Displacement (a.u.)")
plt.title("Wing flapping simulation (demo)")
plt.show()