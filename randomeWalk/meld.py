import numpy as np
import pylab
import random
import math
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress

def random_walk(N, K):
    arrayX = np.zeros(K)
    arrayY = np.zeros(K)

    x = np.zeros(N)
    y = np.zeros(N)

    average = np.zeros(K)

    for k in range(K):
        for i in range(1, N):
            val = random.randint(1, 4)
            if val == 1:
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
            elif val == 2:
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
            elif val == 3:
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
            else:
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 1

        arrayX[k] = x[-1]
        arrayY[k] = y[-1]

        average[k] = math.sqrt(arrayX[k] ** 2 + arrayY[k] ** 2)

    return x, y, average


def calculate_avg_squared_dist(N_values):
    avg_squared_dists = []
    for N in N_values:
        x, y, average = random_walk(N, 1)
        avg_squared_dist = (math.pi / 4) * N
        avg_squared_dists.append(avg_squared_dist)
    return avg_squared_dists


def main():
    N = 3000  # Number of steps
    K = 1000 # Number of Drunkards

    fig, ax = pylab.subplots(2, 2)

    x, y, average = random_walk(N, K)

    N_values = np.arange(100, 1001, 100)

    avg_squared_dists = calculate_avg_squared_dist(N_values)

    N_reshaped = N_values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(N_reshaped, avg_squared_dists)
    avg_squared_dists_pred = model.predict(N_reshaped)

    slope = linregress(N_values, avg_squared_dists).slope

    ax[0, 0].set_title("Random Walk ($n = " + str(N) + "$ steps)")
    ax[0, 0].plot(x, y)

    ax[0, 1].hist(average, bins=200, color='r', alpha=0.5, label='X')
    ax[0, 1].set_title("Random Walk Histogram ($n = " +
                       str(N) + "$ steps and $K = " + str(K) + "$ Drunkards)")

    ax[1, 0].set_title("Hist of E[RN]**2")
    ax[1, 0].hist(np.power(average, 2), bins=200,
                  color='g', alpha=0.5, label='X')

    ax[1, 1].plot(N_values, avg_squared_dists, 'bo', label="E[RN]**2")
    ax[1, 1].plot(N_values, avg_squared_dists_pred, 'r-',
                  linewidth=2, label="Predicted E[RN]**2")
    ax[1, 1].set_title(f"Function slope = {slope}")
    ax[1, 1].set_xlabel('Number of Steps')
    ax[1, 1].set_ylabel('E[RN]**2')
    ax[1, 1].grid(True)
    ax[1, 1].legend()

    pylab.show()


if __name__ == "__main__":
    main()
