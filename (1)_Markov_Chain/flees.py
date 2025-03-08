import numpy as np
import matplotlib.pyplot as plt
import random

def random_jump(N, K):
    for k in range(K):
        s = np.zeros(N)
        pi_vales = np.zeros(N)
        s[0] = 1
        T = [[[1/2], [1/2]],
                [[1], [0]]]
        count = 0

        π1 = np.zeros(N)
        π1[0] = 0

        π2 = np.zeros(N)
        π2[0] = 1

        for i in range(1, N):
            u = random.random()

            if s[i-1] == 1:
                if u >= T[0][1][0]:
                    s[i] = 1
                    count += 1
                else:
                    s[i] = -1
            else:
                s[i] = 1

            if count/i >= 1:
                print(count, i)

            π1[i] = (count/i)
            π2[i] = (1-count/i)

            pi_vales[i] = 1 - π2[i]

        π1_values = np.mean(pi_vales)
        π2_values = 1 - π1_values

    return π1, π2, s, π1_values, π2_values


def main():

    N = 500 # Number of steps in markov chain
    fig, ax = plt.subplots(2, figsize=(12, 10))

    π1, π2, s, π1_values, π2_values = random_jump(N, 1)

    print(π1_values, π2_values)

    ax[0].plot(s)
    ax[0].set_title("Random jump ($n = {}$ steps)".format(N))

    ax[1].plot(π2, label='π2 = {}'.format(π2_values))
    ax[1].plot(π1, label='π1 = {}'.format(round(π1_values, 2)))
    ax[1].set_title("Markov chain for n = {}".format(N))
    ax[1].legend()

    plt.show()


if __name__ == "__main__":
    main()
