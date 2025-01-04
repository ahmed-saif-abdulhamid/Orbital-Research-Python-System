def compute_net_force(r4, positions, G=1.0, masses=[1.0, 1.0, 1.0]):
    net_force = np.zeros(2) 
    for i in range(len(masses)):
        r4i = r4 - positions[i] 
        distance = np.linalg.norm(r4i)
        if distance > 0:  
            net_force += G * masses[i] * r4i / distance**3
    return net_force