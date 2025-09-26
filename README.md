# Flapping-Wing Microbot

A simplified simulation of a flapping-wing micro-robot 🪽

This project models the dynamics of a flapping wing, applies different control strategies (including PID), and provides reproducible visualizations.

---

## 🚀 Features

- **Dynamic model** solved with `scipy.solve_ivp`
- **Controllers**:
  - `zero_control` → free oscillation
  - `sinus_control` → forced sinusoidal oscillation
  - `PID` → angle stabilization
- **Visualization** with `matplotlib`
- **Unit tests** with `pytest`

---

## 📂 Project Structure

```bash
flapping-wing-microbot/
│
├── src/ # Source code
│ ├── dynamics.py # Equations of motion
│ ├── control.py # Controllers (zero, sinusoidal, PID)
│ ├── simulation.py # Simulation runner
│ ├── visualization.py # Plotting and animations
│ └── main.py # Main entry point
│
├── tests/ # Unit tests (pytest)
├── docs/ # Documentation + figures
├── notebooks/ # (optional) Jupyter demos
├── requirements.txt # Dependencies
└── README.md # Project description


```

## ▶️ Usage

Run the main simulation:

```bash
python -m src.main
```
This will generate three plots:

Free oscillation (no control)
The system oscillates naturally without any external input.

Forced oscillation (sinusoidal input)
The wing is driven by a sinusoidal torque, producing regular flapping motion.

PID control (stabilization at target angle)
A PID controller stabilizes the wing around a given reference angle.