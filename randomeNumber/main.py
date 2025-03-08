# 1. Generating randome number from expornential distr. using inverse CDF method (y).
# 2. Reject method

import sys
import matplotlib.pyplot as plt
import numpy as np, numpy
import time
import scipy.stats as stats

def RandomeNumberGeneration():
    number = numpy.random.choice(numpy.arange(
        1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])

    return number

def expon_icdf(p, lambd=1):
    """Inverse CDF of exponential distribution - i.e. quantile function."""
    return -np.log(1-p)/lambd


def expon_cdf(x, lambd=1):
    """CDF of exponetial distribution."""
    return 1 - np.exp(-lambd*x)


def expon_pdf(x, lmabd=1):
    """PDF of exponential distribution."""
    return lmabd*np.exp(-lmabd*x)


def saveToFile(value):
    file_path = "random.dat"

    file_exists = False
    try:
        with open(file_path, 'r') as file_check:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(file_path, 'w' if file_exists else 'a') as out_file:
        out_file.write(f"{value}\n")


def RandomNumberRejectMethod():
    x = np.linspace(-4, 4)

    df = 10
    dist = stats.cauchy()
    upper = dist.pdf(0)

    with plt.xkcd():
#        plt.figure(figsize=(12, 4))
#        plt.subplot(121)
#        plt.plot(x, dist.pdf(x))
#        plt.axhline(upper, color='grey')
#        px = 1.0
#        plt.arrow(px, 0, 0, dist.pdf(1.0)-0.01, linewidth=1,
#                head_width=0.2, head_length=0.01, fc='g', ec='g')
#        plt.arrow(px, upper, 0, -(upper-dist.pdf(px)-0.01), linewidth=1,
#                head_width=0.3, head_length=0.01, fc='r', ec='r')
#        plt.text(px+.25, 0.2, 'Reject', fontsize=16)
#        plt.text(px+.25, 0.01, 'Accept', fontsize=16)
#        plt.axis([-4, 4, 0, 0.4])
#        plt.title('Rejection sampling concepts', fontsize=20)
        plt.subplot(122)
        n = 100000
        # generate from sampling distribution
        u = np.random.uniform(-4, 4, n)
        # accept-reject criterion for each point in sampling distribution
        r = np.random.uniform(0, upper, n)
        # accepted points will come from target (Cauchy) distribution
        v = u[r < dist.pdf(u)]

        print(x)

        plt.plot(x, dist.pdf(x), linewidth=2)

        # Plot scaled histogram
        factor = dist.cdf(4) - dist.cdf(-4)
        hist, bin_edges = np.histogram(v, bins=100, density=True)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2.
        plt.step(bin_centers, factor*hist, linewidth=2)

        plt.axis([-4, 4, 0, 0.4])

        plt.legend()
        plt.show()

RandomNumberRejectMethod()



# start_time = time.time()

# file_path = "random.dat"

# file_exists = False
# try:
#     with open(file_path, 'r') as file_check:
#         file_exists = True
# except FileNotFoundError:
#     pass

# with open(file_path, 'w' if file_exists else 'a') as out_file:
#     arange = numpy.arange(1, 7)

#     for i in range(1,100):
#         out_file.write(f"{RandomeNumberGeneration()}\n")  # Save pi to the file

# stop_time = time.time()
# # Convert seconds to milliseconds
# elapsed_time = (stop_time - start_time) * 1000

# print("The values of pi have been written to 'random.dat'.")
# print(f"Execution time: {elapsed_time:.2f} milliseconds.")


# title = "Randome number plot"

# # Read data from file
# with open("random.dat", 'r') as file:
#     data = [float(line.strip()) for line in file]

# # Calculate the average
# average_value = sum(data) / len(data)

# # Plotting the data
# plt.plot(data, marker='o', linestyle='-')

# # Adding title, labels, and average
# plt.title(title)
# plt.xlabel('Data Points')
# plt.ylabel('Values')
# plt.axhline(y=average_value, color='r', linestyle='--',
#             label=f'Average: {average_value:.2f}')

# # Display the plot with a legend
# plt.legend()
# plt.show()
