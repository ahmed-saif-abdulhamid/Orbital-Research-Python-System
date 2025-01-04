def calculate_energy(y, G, masses):
    r1, r2, r3, r4 = y[:2], y[2:4], y[4:6], y[6:8]
    v1, v2, v3, v4 = y[8:10], y[10:12], y[12:14], y[14:16]
    m1, m2, m3, m4 = masses

    K = 0.5 * (m1 * np.linalg.norm(v1)**2 + m2 * np.linalg.norm(v2)**2 + m3 * np.linalg.norm(v3)**2 + m4 * np.linalg.norm(v4)**2)

    U = -G * (m1 * m2 / np.linalg.norm(r2 - r1) + m1 * m3 / np.linalg.norm(r3 - r1) + m1 * m4 / np.linalg.norm(r4 - r1) + m2 * m3 / np.linalg.norm(r3 - r2) + m2 * m4 / np.linalg.norm(r4 - r2) + m3 * m4 / np.linalg.norm(r4 - r3))

    return K + U
