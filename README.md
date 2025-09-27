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
├── src/ 
│ ├── dynamics.py # Equations of motion
│ ├── control.py # Controllers (zero, sinusoidal, PID)
│ ├── simulation.py # Simulation runner
│ ├── visualization.py # Plotting and animations
│ └── main.py # Main entry point
│
├── tests/ # Unit tests (pytest)
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

## Testing

This project uses **pytest** for unit testing.  
All test files are located in the `tests/` directory.

### Test coverage
- `test_dynamics.py` : verifies the equations of motion implemented in `dynamics.py`.
- `test_control.py` : checks the behavior of the controllers (Zero, Sinusoidal, PID).
- `test_simulation.py` : ensures that simulations run correctly and return valid trajectory data.
- `test_visualization.py` : validates that plotting and animation functions run without errors (note: these tests usually check function calls, not the visual output).

### Running the tests
From the root of the repository:

```bash
python -m pytest -v
