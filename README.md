# An Award-Winning System for Computational Breakthroughs in Orbital Research

## Project Overview
This project features an **Award-Winning System** that was utilized in a groundbreaking research paper in orbital research. Recognized by the **Egyptian Research Institution**, this system earned a prestigious award along with a prize of **20,000 EGP** for its innovative approach to understanding celestial dynamics.

The research explores the stability of the Figure-Eight solution of the three-body problem when perturbed by the introduction of a fourth body. By combining mathematical rigor, numerical simulations, and computational physics, this work provides new insights into the delicate interplay of chaos and stability in gravitational systems.

## Features
- **Dynamic Simulation**: Implements cutting-edge algorithms to simulate gravitational interactions using the REBOUND library.
- **Stability Analysis**: Tests the robustness of stable three-body configurations under various mass, position, and velocity perturbations.
- **Advanced Visualization**: Creates visually engaging trajectory maps and stability plots to highlight key findings.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**:
  - `NumPy` for efficient numerical computations
  - `Matplotlib` for visualization
  - `SciPy` for solving differential equations
  - `REBOUND` for advanced N-body simulations
- **Additional Software**: MATLAB for comparative analysis and extended modeling

## Key Insights
1. **Stability Islands**: Identifies regions of stability amidst chaos for zero-angular momentum solutions.
2. **Energy Conservation**: Analyzes energy fluctuations to assess system stability over time.
3. **Perturbation Effects**: Explores the influence of the fourth body’s mass, velocity, and position on system dynamics.

## Getting Started

### Prerequisites
Ensure the following software is installed on your system:
- Python 3.8+
- Required libraries (install via pip):
  ```bash
  pip install numpy scipy matplotlib rebound
  ```
- Optional: MATLAB for additional analysis (code provided in supplementary materials).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/award-winning-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd award-winning-system
   ```
3. Run the simulation:
   ```bash
   python main.py
   ```

## Usage
1. **Define Parameters**: Configure the masses, initial positions, and velocities of the bodies in the `config.json` file.
2. **Run Simulations**: Execute `main.py` to run the N-body simulations.
3. **Visualize Results**: Use the generated plots and animations in the `output/` directory to analyze system behavior.

### Example
```python
python main.py --mass_4 0.005 --velocity_range 0.1 1.0 --output_path ./output
```

## Outputs
- **Trajectory Plots**: Visual representations of body motion over time.
- **Energy Graphs**: Conservation analysis for total system energy.
- **Stability Maps**: Heatmaps highlighting regions of stability.

## Project Structure
```
award-winning-system/
├── src/
│   ├── simulate.py         # Core simulation logic
│   ├── visualize.py        # Visualization utilities
│   ├── stability_analysis.py  # Stability assessment
├── output/                 # Generated plots and animations
├── README.md               # Project documentation
├── requirements.txt        # Dependencies
├── config.json             # Parameter configuration
└── main.py                 # Entry point
```

## Acknowledgments
This project is inspired by foundational work on the three-body problem and stability analysis by Suvakov, Dmitrašinović, and Montgomery. Special thanks to [STEM October Physics Club](octphysicsclub.org) for their resources and guidance.

## Contact
For questions, suggestions, or collaborations, feel free to reach out:
- **Author**: Ahmed Saif El-Deen Rezk Abd ElHamid
- **Email**: ahmedsaifeldeen1314@gmail.com

