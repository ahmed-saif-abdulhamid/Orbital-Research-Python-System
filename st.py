import numpy as np
from scipy.integrate import solve_ivp
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool

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
m1, m2, m3, m4 = 1.0, 1.0, 1.0, 0.01
r1_0 = [-1.2, 0.1]
r2_0 = [1.1, 0.1]
r3_0 = [0.1, 0.1]
r4_0 = [1.0, 0.1]
v1_0 = [0.1, -0.992852]
v2_0 = [0.1, -0.513024]
v3_0 = [0.1, 0.882922]
v4_0 = [0.1, 0.1]
y0 = np.concatenate((r1_0, r2_0, r3_0, r4_0, v1_0, v2_0, v3_0, v4_0))

# Time span and precision
T = 6.32591398  # Period of one orbit
t_span = (0, 15 * T)
t_eval = np.linspace(*t_span, 10000)  # High-resolution time points

# Solve the system with high precision
solution = solve_ivp(
    four_body_derivatives, t_span, y0, t_eval=t_eval,
    args=(G, m1, m2, m3, m4), method='RK45', rtol=1e-8, atol=1e-10
)

# Extract positions
x1, y1 = solution.y[0], solution.y[1]
x2, y2 = solution.y[2], solution.y[3]
x3, y3 = solution.y[4], solution.y[5]
x4, y4 = solution.y[6], solution.y[7]

# Prepare the Bokeh plot data
output_file("four_body_refined_simulation.html")
source = ColumnDataSource(data=dict(
    x1=x1, y1=y1, x2=x2, y2=y2, x3=x3, y3=y3, x4=x4, y4=y4
))

# Create the Bokeh figure
p = figure(
    title="Refined Four-Body Simulation (High Precision)",
    x_axis_label="x", y_axis_label="y", width=800, height=800
)

# Add trajectories of the bodies
p.line('x1', 'y1', source=source, legend_label="Body 1", color="blue", line_width=2)
p.line('x2', 'y2', source=source, legend_label="Body 2", color="green", line_width=2)
p.line('x3', 'y3', source=source, legend_label="Body 3", color="red", line_width=2)
p.line('x4', 'y4', source=source, legend_label="Body 4 (Planet)", color="purple", line_width=2)

# Add hover tool for interactive data
hover = HoverTool(tooltips=[
    ("Body 1", "(@x1, @y1)"),
    ("Body 2", "(@x2, @y2)"),
    ("Body 3", "(@x3, @y3)"),
    ("Body 4 (Planet)", "(@x4, @y4)")
])
p.add_tools(hover)

# Restore legend visibility
p.legend.visible = True
p.legend.location = "top_left"

# Show the plot
show(p)
