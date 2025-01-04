import rebound
import numpy as np
import matplotlib.pyplot as plt

def setup_simulation(mass4=0.001, pos4=(1.0, 0.0, 0.0), vel4=(0.0, 0.5, 0.0), sim_time=100):
    sim = rebound.Simulation()
    sim.units = ('AU', 'yr', 'Msun')
    sim.add(m=1.0, x=-1, y=0, z=0, vx=0, vy=-0.5, vz=0)
    sim.add(m=1.0, x=1, y=0, z=0, vx=0, vy=0.5, vz=0)
    sim.add(m=1.0, x=0, y=1, z=0, vx=-0.5, vy=0, vz=0)
    sim.add(m=mass4, x=pos4[0], y=pos4[1], z=pos4[2], vx=vel4[0], vy=vel4[1], vz=vel4[2])
    sim.move_to_com()
    return sim

def run_simulation(sim, sim_time=100, steps=1000):
    times = np.linspace(0, sim_time, steps)
    positions = []
    for t in times:
        sim.integrate(t)
        positions.append([[p.x, p.y, p.z] for p in sim.particles])
    return times, np.array(positions)

def plot_trajectories(times, positions):
    plt.figure(figsize=(8, 6))
    for i in range(4):
        plt.plot(positions[:, i, 0], positions[:, i, 1], label=f"Body {i+1}")
    plt.xlabel("x [AU]")
    plt.ylabel("y [AU]")
    plt.title("Trajectories of the Four-Body System")
    plt.legend()
    plt.grid(True)
    plt.show()

if name == "__main__":
    mass4 = 0.001
    pos4 = (1.0, 0.0, 0.0)
    vel4 = (0.0, 0.5, 0.0)
    sim = setup_simulation(mass4=mass4, pos4=pos4, vel4=vel4, sim_time=50)
    times, positions = run_simulation(sim, sim_time=50, steps=500)
    plot_trajectories(times, positions)