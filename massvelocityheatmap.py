def four_body_derivatives(t, y, G, m1, m2, m3, m4):
    r1, r2, r3, r4 = y[:2], y[2:4], y[4:6], y[6:8]
    v1, v2, v3, v4 = y[8:10], y[10:12], y[12:14], y[14:16]
    r14, r24, r34 = np.linalg.norm(r4 - r1), np.linalg.norm(r4 - r2), np.linalg.norm(r4 - r3)
    a4 = G * (m1 * (r1 - r4) / r14**3 + m2 * (r2 - r4) / r24**3 + m3 * (r3 - r4) / r34**3)
    return np.concatenate((v1, v2, v3, v4, np.zeros(6), a4))
