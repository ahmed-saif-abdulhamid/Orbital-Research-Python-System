import numpy as np
import matplotlib.pyplot as plt

def compute_net_force(r4, positions, G=1.0, masses=[1.0, 1.0, 1.0]):
    net_force = np.zeros(2)
    for i in range(len(masses)):
        r4i = r4 - positions[i]
        distance = np.linalg.norm(r4i)
        if distance > 0:
            net_force += G * masses[i] * r4i / distance**3
    return net_force

positions = np.array([
    [-0.97000436, 0.24308753],
    [0.97000436, -0.24308753],
    [0.0, 0.0]
])

x_range = np.linspace(0.1, 10.0, 100)
forces = []

for x in x_range:
    r4 = np.array([x, 0.0])
    net_force = compute_net_force(r4, positions)
    force_magnitude = np.linalg.norm(net_force)
    forces.append(force_magnitude)

plt.figure(figsize=(10, 6))
plt.plot(x_range, forces, label="Net Force Magnitude")
plt.axvline(0.5, color='gray', linestyle='--', label="Lower Bound (0.5)")
plt.axvline(2.0, color='black', linestyle='--', label="Upper Bound (2.0)")
plt.xlabel("Distance from Center of Mass")
plt.ylabel("Net Force Magnitude")
plt.title("Net Gravitational Force on the Fourth Body vs. Distance")
plt.legend()
plt.grid(True)
plt.show()
