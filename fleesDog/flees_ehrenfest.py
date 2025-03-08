import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import binom


def random_jump(t, p, K):
    s = np.zeros(t)
    s[0] = 1

    Na = np.full(t, K)
    Nb = np.zeros(t)

    percentage = 0

    k = 0

    while (k < K):
        for i in range(1, t):
            u = random.random()
            if u >= p:
                s[i] = 0

                Na[i] = Na[i-1] - 1 if Na[i-1] > 0 else Na[i-1]
                Nb[i] = Nb[i-1] + 1 if Nb[i-1] < K else Nb[i-1]
            else:
                s[i] = 1
        k += 1
        if (percentage != round(k / K * 100, 1)):
            percentage = round(k / K * 100, 1)
            print(percentage, "%")
    return s, Na, Nb


def jump_asymptotics_analysis(t, K, p):
    # Adjusted length to t+1 to account for all possible counts from 0 to t
    p_values = np.zeros(t+1)
    for _ in range(K):
        # Simulation of fleas jumping with probability p
        count = 0
        for _ in range(t):
            if random.random() < p:
                count += 1
        # Update the histogram for the observed count of fleas on dog A
        p_values[count] += 1
    p_values /= K  # Normalize to get probability estimates

    # Theoretical binomial distribution calculated for all possible outcomes from 0 to t
    theoretical_pn = binom.pmf(np.arange(t+1), t, p)

    return p_values, theoretical_pn


def main():
    t = 10000 # Total time
    t_shown = 100
    K = 1000 # Number of fleas
    p = 0.5  # Probability of jumping
    fig, ax = plt.subplots(3, figsize=(12, 15))

    simulation_results, theoretical_pn = jump_asymptotics_analysis(t, K, p)
    s, Na, Nb = random_jump(t, p, K)

    ax[0].plot(s[:t_shown])
    ax[0].set_title(f"Random jump, where t = {t_shown})")

    ax[1].plot(Na, 'r-', label=f'Na')
    ax[1].plot(Nb, 'b-', label=f'Nb')
    ax[1].set_title(
        f"$t = {t}$ steps and $k = {K}$ fleas with $p = {p}$")
    ax[1].legend()

    # Plotting simulation results and theoretical distribution
    ax[2].scatter(np.arange(t+1), simulation_results,
                  color='blue', label='Simulation')
    ax[2].plot(np.arange(t+1), theoretical_pn, 'r-',
               label='Theoretical Binomial Distribution')
    ax[2].set_title(
        f"Asymptotic Probability P(n) for $t = {t}$ over $k = {K}$ flees and $p = {p}$")
    ax[2].legend()

    plt.show()


if __name__ == "__main__":
    main()
