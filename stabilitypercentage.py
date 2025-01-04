def evaluate_stability(x4, y4, x1, y1, x2, y2):
    r41 = np.sqrt((x4 - x1)**2 + (y4 - y1)**2)
    r42 = np.sqrt((x4 - x2)**2 + (y4 - y2)**2)
    stable_points = ((0.5 <= r41) & (r41 <= 2.0)) & ((0.5 <= r42) & (r42 <= 2.0))
    return np.sum(stable_points) / len(r41) * 100