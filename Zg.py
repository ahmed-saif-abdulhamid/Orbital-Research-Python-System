import numpy as np
import matplotlib.pyplot as plt

# Function to compute net force on the fourth body
def compute_net_force(r4, positions, G=1.0, masses=[1.0, 1.0, 1.0]):
    net_force = np.zeros(2)  # Initialize force vector
    for i in range(len(masses)):
        r4i = r4 - positions[i]  # Vector from body i to body 4
        distance = np.linalg.norm(r4i)
        if distance > 0:  # Avoid division by zero
            net_force += G * masses[i] * r4i / distance**3
    return net_force

# Positions of the three primary bodies (assumed symmetric figure-eight)
positions = np.array([
    [-0.97000436, 0.24308753],   # Body 1
    [0.97000436, -0.24308753],   # Body 2
    [0.0, 0.0]                   # Body 3
])

# Test positions for the fourth body along the x-axis
x_range = np.linspace(0.1, 10.0, 100)  # Vary distance from 0.1 to 3.0
forces = []

# Compute net force magnitude at each test position
for x in x_range:
    r4 = np.array([x, 0.0])  # Test position along x-axis
    net_force = compute_net_force(r4, positions)
    force_magnitude = np.linalg.norm(net_force)
    forces.append(force_magnitude)

# Plot net force magnitude vs. distance
plt.figure(figsize=(10, 6))
plt.plot(x_range, forces, label="Net Force Magnitude")
plt.axvline(0.5, color='gray', linestyle='--', label="Lower Bound (0.5)")
plt.axvline(2.0, color='black', linestyle='--', label="Upper Bound (2.0)")
plt.xlabel("Distance from Center of Mass")
plt.ylabel("Net Force Magnitude")
plt.title("Net Gravitational Force on the Fourth Body vs. Distance")
plt.legend()
plt.grid()
plt.show()
