import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Function to compute the derivatives for the 4-body problem
def four_body_derivatives(t, y, G, m1, m2, m3, m4):
    r1, r2, r3, r4 = y[:2], y[2:4], y[4:6], y[6:8]
    v1, v2, v3, v4 = y[8:10], y[10:12], y[12:14], y[14:16]

    # Distances
    r12 = np.linalg.norm(r2 - r1)
    r13 = np.linalg.norm(r3 - r1)
    r14 = np.linalg.norm(r4 - r1)
    r23 = np.linalg.norm(r3 - r2)
    r24 = np.linalg.norm(r4 - r2)
    r34 = np.linalg.norm(r4 - r3)

    # Accelerations due to gravitational forces
    a1 = G * (m2 * (r2 - r1) / r12**3 + m3 * (r3 - r1) / r13**3 + m4 * (r4 - r1) / r14**3)
    a2 = G * (m1 * (r1 - r2) / r12**3 + m3 * (r3 - r2) / r23**3 + m4 * (r4 - r2) / r24**3)
    a3 = G * (m1 * (r1 - r3) / r13**3 + m2 * (r2 - r3) / r23**3 + m4 * (r4 - r3) / r34**3)
    a4 = G * (m1 * (r1 - r4) / r14**3 + m2 * (r2 - r4) / r24**3 + m3 * (r3 - r4) / r34**3)

    return np.concatenate((v1, v2, v3, v4, a1, a2, a3, a4))

# Constants and initial conditions
G = 1.0
m1, m2, m3, m4 = 1.0, 1.0, 1.0, 0.002
r1_0 = [-0.97000436, 0.24308753]
r2_0 = [0.97000436, -0.24308753]
r3_0 = [0.0, 0.0]
r4_0 = [-0.1414213, -0.1414213]
v1_0 = [0.466203685, 0.43236573]
v2_0 = [0.466203685, 0.43236573]
v3_0 = [-0.93240737, -0.86473146]
v4_0 = [-0.1414213, -0.1414213]
y0 = np.concatenate((r1_0, r2_0, r3_0, r4_0, v1_0, v2_0, v3_0, v4_0))

# Simulation periods and titles
periods = [1, 3, 5, 10]
titles = ["1 Period", "3 Periods", "5 Periods", "10 Periods"]

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

# Shared legend data
legend_labels = ["Body 1", "Body 2", "Body 3", "Body 4"]

# Simulate for each period and adjust axis limits
for i, period in enumerate(periods):
    t_span = (0, period * 6.32591398)
    t_eval = np.linspace(*t_span, 5000)

    # Solve the system
    solution = solve_ivp(
        four_body_derivatives, t_span, y0, t_eval=t_eval,
        args=(G, m1, m2, m3, m4), method='RK45', rtol=1e-8, atol=1e-10
    )

    # Extract positions
    x1, y1 = solution.y[0], solution.y[1]
    x2, y2 = solution.y[2], solution.y[3]
    x3, y3 = solution.y[4], solution.y[5]
    x4, y4 = solution.y[6], solution.y[7]

    # Determine dynamic axis limits
    x_all = np.concatenate([x1, x2, x3, x4])
    y_all = np.concatenate([y1, y2, y3, y4])
    x_min, x_max = np.min(x_all), np.max(x_all)
    y_min, y_max = np.min(y_all), np.max(y_all)
    axis_buffer = 0.1 * (x_max - x_min)  # Add a small buffer

    # Plot trajectories
    axes[i].plot(x1, y1, color="blue", linewidth=1.5, label="Body 1")
    axes[i].plot(x2, y2, color="green", linewidth=1.5, label="Body 2")
    axes[i].plot(x3, y3, color="red", linewidth=1.5, label="Body 3")
    axes[i].plot(x4, y4, color="purple", linewidth=1.5, label="Body 4")
    axes[i].set_title(titles[i])
    axes[i].set_xlim(x_min - axis_buffer, x_max + axis_buffer)
    axes[i].set_ylim(y_min - axis_buffer, y_max + axis_buffer)
    axes[i].grid()

# Add a global legend outside the grid
fig.legend(legend_labels, loc='center right', frameon=False)

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.suptitle("Four-Body Simulation Over Different Periods", fontsize=14, y=1.02)
plt.show()
