import random
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from functools import partial


def simulate_spins(T_star, MCS, s, grid_size=10):
    grid = np.ones((grid_size, grid_size), dtype=int) * s
    spin_changes = []

    m = 0.0
    ae = 0.0
    ae2 = 0.0

    for k in range(MCS):
        # Choose a random position in the grid
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)

        dE = 2 if grid[x, y] == 1 else -2
        n = random.uniform(0.0, 1.0)

        if n < math.exp(-dE / T_star):
            grid[x, y] = -grid[x, y]

        if k > 1000:
            m += grid[x, y]
            ae += grid[x, y]
            ae2 += grid[x, y] * grid[x, y]
            spin_changes.append(grid.copy())

    m /= (MCS - 1000)
    ae /= (MCS - 1000)
    ae2 /= (MCS - 1000)

    Cv = (ae2 - ae**2) / (T_star**2)
    return m, Cv, spin_changes


def update(frame, ax, spin_changes):
    ax.clear()
    ax.imshow(spin_changes[frame], cmap='gray', vmin=-1, vmax=1)
    ax.set_title(f'Step {frame + 1001}')
    ax.axis('off')


def main():
    T_star = 2.0  # example temperature
    MCS = 5000    # Reduced to speed up the animation
    s = 1
    grid_size = 10

    m, Cv, spin_changes = simulate_spins(T_star, MCS, s, grid_size)

    fig, ax = plt.subplots(figsize=(6, 6))
    ani = FuncAnimation(fig, partial(
        update, ax=ax, spin_changes=spin_changes), frames=len(spin_changes), repeat=False)

    plt.show()


if __name__ == "__main__":
    main()
