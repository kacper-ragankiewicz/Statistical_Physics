import numpy as np
import matplotlib.pyplot as plt
import random
from multiprocessing import Pool
import os


def single_walk(N):
    """
    Simulate a single random walk of N steps in 2D.
    Returns the final position and the Euclidean distance from the origin.
    """
    directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    steps = directions[np.random.randint(0, 4, size=N)]
    walk = np.cumsum(steps, axis=0)
    return walk[-1]


def random_walk(N, K):
    """
    Simulates a random walk in 2D for N steps and K walkers.
    Utilizes multiprocessing to speed up the simulation across multiple CPU cores.
    Returns the final positions and the Euclidean distances from the origin.
    """
    with Pool(os.cpu_count()) as pool:
        results = pool.map(single_walk, [N]*K)

    final_positions = np.array(results)
    distances = np.linalg.norm(final_positions, axis=1)
    return final_positions, distances


def main():
    N = 3000000  # Number of steps
    K = 100000   # Number of Drunkards

    fig, ax = plt.subplots(2, 2, figsize=(12, 10))

    # Perform random walk
    final_positions, distances = random_walk(N, K)

    # Plot the walk of the first random walker for visualization
    ax[0, 0].plot(final_positions[:, 0],
                  final_positions[:, 1], 'o', markersize=3)
    ax[0, 0].set_title("End Positions of Random Walks")

    # Histogram of distances
    ax[0, 1].hist(distances, bins=200, color='red', alpha=0.5)
    ax[0, 1].set_title("Histogram of Distances")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
