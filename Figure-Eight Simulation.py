import numpy as np
from scipy.integrate import solve_ivp
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool

def three_body_derivatives(t, y, G, m1, m2, m3):
    r1, r2, r3 = y[:2], y[2:4], y[4:6]
    v1, v2, v3 = y[6:8], y[8:10], y[10:12]

    r12 = np.linalg.norm(r2 - r1)
    r13 = np.linalg.norm(r3 - r1)
    r23 = np.linalg.norm(r3 - r2)

    a1 = G * m2 * (r2 - r1) / r12**3 + G * m3 * (r3 - r1) / r13**3
    a2 = G * m1 * (r1 - r2) / r12**3 + G * m3 * (r3 - r2) / r23**3
    a3 = G * m1 * (r1 - r3) / r13**3 + G * m2 * (r2 - r3) / r23**3

    return np.concatenate((v1, v2, v3, a1, a2, a3))


G = 1.0 
m1, m2, m3 = 1.0, 1.0, 1.0 

r1_0 = np.array([-0.97000436, 0.24308753])
r2_0 = np.array([0.97000436, -0.24308753])
r3_0 = np.array([0.0, 0.0])

v1_0 = np.array([0.4662036850, 0.4323657300])
v2_0 = np.array([0.4662036850, 0.4323657300])
v3_0 = np.array([-0.93240737, -0.86473146])

y0 = np.concatenate((r1_0, r2_0, r3_0, v1_0, v2_0, v3_0))

T = 6.32591398  
t_span = (0, 5 * T)  
t_eval = np.linspace(*t_span, 1000) 

solution = solve_ivp(
    three_body_derivatives, t_span, y0, t_eval=t_eval,
    args=(G, m1, m2, m3), method='RK45', rtol=1e-9, atol=1e-9
)

x1, y1 = solution.y[0], solution.y[1]
x2, y2 = solution.y[2], solution.y[3]
x3, y3 = solution.y[4], solution.y[5]

output_file("figure_eight_simulation.html")
source = ColumnDataSource(data=dict(
    x1=x1, y1=y1, x2=x2, y2=y2, x3=x3, y3=y3
))

p = figure(
    title="Figure-Eight 3-Body Problem Simulation",
    x_axis_label="x", y_axis_label="y", width=800, height=800
)

p.line('x1', 'y1', source=source, legend_label="Body 1", color="blue", line_width=2)
p.line('x2', 'y2', source=source, legend_label="Body 2", color="green", line_width=2)
p.line('x3', 'y3', source=source, legend_label="Body 3", color="red", line_width=2)

hover = HoverTool(tooltips=[
    ("Body 1", "(@x1, @y1)"),
    ("Body 2", "(@x2, @y2)"),
    ("Body 3", "(@x3, @y3)")
])
p.add_tools(hover)
p.legend.location = "top_left"

show(p)
