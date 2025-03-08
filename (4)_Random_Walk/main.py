import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def random_walk(N, K):
    # Simulate random walk for K Drunkards
    positions = np.zeros(K)
    for _ in range(N):
        steps = np.random.choice([-1, 1], size=K)
        positions += steps
    return positions


def calculate_variance(N_values, K):
    variances = []
    for N in N_values:
        positions = random_walk(N, K)
        variance = np.var(positions)
        variances.append(variance)
    return np.array(variances)


def main():
    N = 100  # Number of steps
    K = 300  # Number of Drunkards

    N_values = np.arange(100, 1001, 100)

    variances = calculate_variance(N_values, K)

    # Compute logarithms of N and V(Xn)
    log_N_values = np.log(N_values)
    log_variances = np.log(variances)

    # Perform linear regression on log(N) and log(V(Xn))
    log_N_values_reshaped = log_N_values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(log_N_values_reshaped, log_variances)
    log_variances_pred = model.predict(log_N_values_reshaped)

    # Perform random walk
    positions = random_walk(N, K)

    fig, axis = plt.subplots(2, 2)

    position_one = np.cumsum(np.random.choice([-1, 1], size=N))
    position_two = np.cumsum(np.random.choice([-1, 1], size=N))
    position_three = np.cumsum(np.random.choice([-1, 1], size=N))

    axis[0, 0].plot(position_one, label='Drunkard One')
    axis[0, 0].plot(position_two, label='Drunkard Two')
    axis[0, 0].plot(position_three, label='Drunkard Three')
    axis[0, 0].set_xlabel('Steps')
    axis[0, 0].set_ylabel('Position')
    axis[0, 0].set_title(f'Random Walk for Drunkards for N = {N}')
    axis[0, 0].grid(True)
    axis[0, 0].legend()

    # Create histogram with more bins
    axis[0, 1].hist(positions, bins=300, density=False, alpha=0.5, color='b')

    axis[0, 1].set_title(
        f"Final Positions of Drunkards for N = {N} and K = {K}")
    axis[0, 1].set_xlabel('Xn')
    axis[0, 1].set_ylabel('Number of Drunkards')
    axis[0, 1].grid(True)

    axis[1, 0].plot(log_N_values, log_variances, 'bo',
                    label='log(Variance of Final Positions)')
    axis[1, 0].plot(log_N_values, log_variances_pred, color='red',
                    linewidth=2, label='Linear Regression')

    axis[1, 0].set_title(
        'Drunkard Linear Regression')
    axis[1, 0].set_xlabel('log(Number of Steps)')
    axis[1, 0].set_ylabel('log(Variance of Final Positions)')
    axis[1, 0].grid(True)
    axis[1, 0].legend()

    fig.suptitle('N - number of steps, K - number of drunkard')

    plt.show()


if __name__ == "__main__":
    main()
