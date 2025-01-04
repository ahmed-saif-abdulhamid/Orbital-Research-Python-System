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
m1, m2, m3, m4 = 1.0, 1.0, 1.0, 0.006
r1_0 = [-0.97000436, 0.24308753]
r2_0 = [0.97000436, -0.24308753]
r3_0 = [0.0, 0.0]
r4_0 = [0.1, 0.15]
v1_0 = [0.466203685, 0.43236573]
v2_0 = [0.466203685, 0.43236573]
v3_0 = [-0.93240737, -0.86473146]
v4_0 = [0.1, 0.1]
y0 = np.concatenate((r1_0, r2_0, r3_0, r4_0, v1_0, v2_0, v3_0, v4_0))

# Time span and precision
T = 6.32591398  # Period of one orbit
t_span = (0, 5 * T)
t_eval = np.linspace(*t_span, 10000)

# Solve the system with high precision
solution = solve_ivp(
    four_body_derivatives, t_span, y0, t_eval=t_eval, 
    args=(G, m1, m2, m3, m4), method='RK45', rtol=1e-10, atol=1e-12
)

# Extract positions
x1, y1 = solution.y[0], solution.y[1]
x2, y2 = solution.y[2], solution.y[3]
x3, y3 = solution.y[4], solution.y[5]
x4, y4 = solution.y[6], solution.y[7]

# Calculate distances from the fourth body to each of the other three bodies
r41 = np.sqrt((x4 - x1)**2 + (y4 - y1)**2)
r42 = np.sqrt((x4 - x2)**2 + (y4 - y2)**2)
r43 = np.sqrt((x4 - x3)**2 + (y4 - y3)**2)

# Plot distances over time
plt.figure(figsize=(10, 6))
plt.plot(t_eval, r41, label="Distance to Body 1 (r41)", color='blue')
plt.plot(t_eval, r42, label="Distance to Body 2 (r42)", color='green')
plt.plot(t_eval, r43, label="Distance to Body 3 (r43)", color='red')
plt.axhline(0.5, color='gray', linestyle='--', label="Lower Stability Bound (0.5)")
plt.axhline(2.0, color='black', linestyle='--', label="Upper Stability Bound (2.0)")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Distances from the Fourth Body to the Three Primary Bodies")
plt.legend()
plt.grid()
plt.show()
