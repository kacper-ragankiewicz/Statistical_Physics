import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_particles = 100  # Total number of particles
num_iterations = 1000  # Number of iterations to simulate
urn_A = num_particles  # Initially, all particles are in urn A
urn_B = 0  # Urn B starts empty

# To store the number of particles in urn A over time
history_A = []

# Simulation
for _ in range(num_iterations):
    history_A.append(urn_A)
    # Choose a particle at random to consider for moving
    if np.random.rand() < 0.8:  # 80% chance to consider moving a particle from A to B
        if urn_A > 0:  # Only move if there are particles in A
            urn_A -= 1
            urn_B += 1
    else:  # 20% chance to consider moving a particle from B to A
        if urn_B > 0:  # Only move if there are particles in B
            urn_A += 1
            urn_B -= 1

# Plotting the results
plt.plot(history_A, label='Urn A')
plt.plot([num_particles - x for x in history_A], label='Urn B')
plt.xlabel('Time')
plt.ylabel('Number of Particles')
plt.title('Ehrenfest Model: Particle Distribution Over Time with p=0.8')
plt.legend()
plt.show()
