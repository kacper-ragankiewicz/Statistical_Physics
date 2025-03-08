import numpy as np
import matplotlib.pyplot as plt
import random
import math
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress


def random_walk(N, K):
    """
    Simulates a random walk in 2D for N steps and K walkers.
    Returns the final positions and the Euclidean distances from the origin.
    """
    directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    walks = np.zeros((K, N, 2))
    for k in range(K):
        steps = directions[np.random.randint(0, 4, size=N-1)]
        walks[k, 1:] = steps.cumsum(axis=0)

    distances = np.linalg.norm(walks[:, -1, :], axis=1)
    return walks, distances


def calculate_avg_squared_dist(N_values):
    """
    Calculates the average squared distance for a set of steps.
    Theoretical calculation using (pi/4) * N.
    """
    return [(math.pi / 4) * N for N in N_values]




def main():
    # 36 GB RAM
    # N = 30000  # Number of steps
    # K = 100000  # Number of Drunkards

    N = 3000
    K = 1000

    fig, ax = plt.subplots(2, 2, figsize=(12, 10))

    # Perform random walk and plot the first one for visualization
    walks, distances = random_walk(N, K)
    ax[0, 0].plot(walks[0, :, 0], walks[0, :, 1])
    ax[0, 0].set_title("Random Walk ($n = {}$ steps)".format(N))

    # Histogram of distances
    ax[0, 1].hist(distances, bins=200, color='red', alpha=0.5)
    ax[0, 1].set_title(
        "Histogram of Distances ($n = {}$, $K = {}$)".format(N, K))

    # Prepare data for linear regression
    N_values = np.arange(100, 3001, 100)
    avg_squared_dists = calculate_avg_squared_dist(N_values)

    ax[1, 0].set_title("Hist of E[RN]**2")
    ax[1, 0].hist(np.power(distances, 2), bins=200,
                  color='g', alpha=0.5, label='X')

    # Fit linear regression
    model = LinearRegression()
    model.fit(N_values.reshape(-1, 1), avg_squared_dists)
    predictions = model.predict(N_values.reshape(-1, 1))

    slope = linregress(N_values, avg_squared_dists).slope

    # Plotting the linear regression results
    slope, _, _, _, _ = linregress(N_values, avg_squared_dists)
    ax[1, 1].plot(N_values, avg_squared_dists, 'bo', label="Observed E[RN]**2")
    ax[1, 1].plot(N_values, predictions, 'r-',
                  linewidth=2, label="Predicted E[RN]**2")
    ax[1, 1].set_title(
        f"Value of slope = {slope}")
    ax[1, 1].set_xlabel(
        f'Number of Steps, N values = {N_values}')
    ax[1, 1].set_ylabel('E[RN]**2')
    ax[1, 1].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
