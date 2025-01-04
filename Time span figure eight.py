T = 6.32591398
t_span = (0, 10 * T)
t_eval = np.linspace(*t_span, 10000)

solution = solve_ivp(three_body_derivatives, t_span, y0, t_eval=t_eval, args=(G,), rtol=1e-10, atol=1e-12)