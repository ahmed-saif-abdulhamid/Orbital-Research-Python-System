def calculate_angular_momentum(y, masses):
    r1, r2, r3, r4 = y[:2], y[2:4], y[4:6], y[6:8]
    v1, v2, v3, v4 = y[8:10], y[10:12], y[12:14], y[14:16]
    m1, m2, m3, m4 = masses

    L = (m1 * np.cross(r1, v1) + m2 * np.cross(r2, v2) + m3 * np.cross(r3, v3) + m4 * np.cross(r4, v4))
    return L