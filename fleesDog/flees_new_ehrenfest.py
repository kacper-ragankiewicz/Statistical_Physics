import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import binom
from tqdm import tqdm


def random_jump(t, p, K):
    s = np.zeros(t)
    s[0] = 1

    Na = np.full(t, K)
    Nb = np.zeros(t)

    for _ in tqdm(range(K)):
        for i in range(1, t):
            u = random.random()
            if u >= p:
                s[i] = 0
                if Na[i-1] > 0:
                    Na[i] = Na[i-1] - 1
                    Nb[i] = Nb[i-1] + 1
                else:
                    Na[i] = Na[i-1]
                    Nb[i] = Nb[i-1]
            else:
                s[i] = 1
                if Nb[i-1] > 0:
                    Na[i] = Na[i-1] + 1
                    Nb[i] = Nb[i-1] - 1
                else:
                    Na[i] = Na[i-1]
                    Nb[i] = Nb[i-1]
    return s, Na, Nb


def jump_asymptotics_analysis(t, K, p):
    p_values = np.zeros(K+1)
    random.seed(42)  # Set seed for reproducibility

    for _ in tqdm(range(K)):
        fleas_on_A = K // 2  # Start from the middle
        for _ in range(t):
            if random.random() <= p:
                fleas_on_A = min(fleas_on_A + 1, K)
            else:
                fleas_on_A = max(fleas_on_A - 1, 0)
        p_values[fleas_on_A] += 1

    p_values /= K  # Normalize to get probability estimates

    theoretical_pn = binom.pmf(np.arange(K+1), K, p)
    return p_values, theoretical_pn


def main():
    t = 1000  # Total time, increased to ensure convergence
    t_shown = 100
    K = 1000  # Number of fleas
    p = 0.4  # Probability of jumping
    fig, ax = plt.subplots(3, figsize=(12, 15))

    # Get the simulation results and theoretical distribution
    simulation_results, theoretical_pn = jump_asymptotics_analysis(t, K, p)

    # Get the random jump results
    s, Na, Nb = random_jump(t, p, K)

    ax[0].plot(s[:t_shown])
    ax[0].set_title(f"Random jump, where t = {t_shown})")

    ax[1].plot(Na, 'r-', label='Na')
    ax[1].plot(Nb, 'b-', label='Nb')
    ax[1].set_title(
        f"$t = {t}$ steps and $k = {K}$ fleas with $p = {p}$")
    ax[1].legend()

    # Plot simulation results and theoretical binomial distribution
    x_values = np.arange(K+1)

    for x in range(0, K+ 1):
        print(x_values[x], simulation_results[x])

    ax[2].bar(x_values, simulation_results, alpha=0.6,
              color='blue', label='Simulation')
    ax[2].plot(x_values, theoretical_pn, 'r-', lw=2,
               label='Theoretical Binomial Distribution')
    ax[2].set_xlabel('Number of Fleas on Dog A')
    ax[2].set_ylabel('Probability')
    ax[2].set_title(
        f"Asymptotic Probability P(n) for $t = {t}$ over $k = {K}$ fleas and $p = {p}$")
    ax[2].legend()

    plt.show()


if __name__ == "__main__":
    main()
