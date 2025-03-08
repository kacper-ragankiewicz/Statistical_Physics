import random
import math
import matplotlib.pyplot as plt


def simulate_spins(T_star, MCS, s):
    m = 0.0
    ae = 0.0
    ae2 = 0.0

    for k in range(MCS):
        dE = 2 if s == 1 else -2
        n = random.uniform(0.0, 1.0)

        if n < math.exp(-dE / T_star):
            s = -s

        if k > 1000:
            m += s
            ae += s
            ae2 += s * s

    m /= (MCS - 1000)
    ae /= (MCS - 1000)
    ae2 /= (MCS - 1000)

    Cv = (ae2 - ae**2) / (T_star**2)
    return m, Cv


def main():
    T_STAR_MIN = 0.1
    T_STAR_MAX = 20.0
    MCS = 3000
    INITIAL_SPIN = 1

    temperatures = []
    magnetizations = []
    specific_heats = []
    theoretical_magnetizations = []
    theoretical_specific_heats = []

    for T_star in [i * 0.001 for i in range(int(T_STAR_MIN * 1000), int(T_STAR_MAX * 1000))]:
        if T_star == 0.0:
            continue

        m, Cv = simulate_spins(T_star, MCS, INITIAL_SPIN)

        m_teor = math.tanh(1 / T_star)
        CV_teor = (1 - (math.tanh(1 / T_star) ** 2)) / (T_star**2)

        temperatures.append(T_star)
        magnetizations.append(m)
        specific_heats.append(Cv)
        theoretical_magnetizations.append(m_teor)
        theoretical_specific_heats.append(CV_teor)

    # Plotting
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.plot(temperatures, magnetizations, label="Simulated m", color='b')
    plt.plot(temperatures, theoretical_magnetizations,
             label="Theoretical m", linestyle='dashed', color='r')
    plt.xlabel('T*')
    plt.ylabel('Magnetization')
    plt.title('Magnetization vs Temperature')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(temperatures, specific_heats, label="Simulated Cv", color='b')
    plt.plot(temperatures, theoretical_specific_heats,
             label="Theoretical Cv", linestyle='dashed', color='r')
    plt.xlabel('T*')
    plt.ylabel('Specific Heat')
    plt.title('Specific Heat vs Temperature')
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
