
import math
import matplotlib.pyplot as plt
import numpy as np

C = 2

def f(x):
    return 4*x**2*np.exp(-2*x)
def g(x):
    return 0.5*np.exp(-x/2)

def randome_generator(C):
    num_generated = 0
    generated_numbers = []

    while num_generated < 10000:
        u1 = np.random.uniform(0,1)
        y = -2*np.log(u1)
        u2 = np.random.uniform(0,1)
        PDF = u2 * C * g(y)
        if PDF < f(y):
            generated_numbers.append(y)
            num_generated += 1
    x_values = np.linspace(min(generated_numbers), max(generated_numbers))
    PDF_curve = f(x_values)

    plt.hist(generated_numbers, bins=50, density=True, alpha=0.7, label="Generated Numbers")
    plt.plot(x_values, PDF_curve, color='red', label='PDF')
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.title('Histogram of Generated Numbers')
    plt.legend()
    plt.show()


randome_generator(2)
