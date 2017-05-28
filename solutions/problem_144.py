import numpy as np

def compute(verbose=False):
    def next_pos(pos, vel): # vector vel departing position pos
        m = vel[1]/vel[0]
        b = pos[1] - m*pos[0]
        possible_x = np.roots([m**2+4, 2*m*b, b**2-100])
        x = max(possible_x, key=lambda x: abs(x-pos[0])) # Take the farthest x from current one
        y = m*x + b
        return np.array((x,y))

    def next_vel(pos, vel): # vector vel incident at position pos
        norm = np.array((4*pos[0], pos[1]))
        norm = -norm / np.linalg.norm(norm)
        vel = vel - 2 * np.dot(vel, norm) * norm
        return vel #/ np.linalg.norm(vel)

    pos = np.array((0.0, 10.1))
    vel = np.array((1.4, -19.7))
    n = 0
    while abs(pos[0]) >= 0.01 or pos[1] < 0 or n == 0:
        pos = next_pos(pos, vel)
        vel = next_vel(pos, vel)
        n += 1
    return n-1, 'Number of reflections inside the white cell'
