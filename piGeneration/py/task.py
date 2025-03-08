import random
import time
from datetime import datetime
import sys

if len(sys.argv) != 2:
    print("Usage: python task.py <l>")
    sys.exit(1)

l = int(sys.argv[1])
lk = 0

# Rest of your Python script remains unchanged


# Seed for random number generation
random.seed(time.time())

# Measure the start time
start_time = time.time()

file_path = "data/pi_values.dat"

# Check if the file exists
file_exists = False
try:
    with open(file_path, 'r') as file_check:
        file_exists = True
except FileNotFoundError:
    pass

# Open the file with truncation if it exists
with open(file_path, 'w' if file_exists else 'a') as out_file:
    for i in range(1, l + 1):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1.0:
            print(lk)
            lk += 1

        pi = lk * 4.0 / i  # Calculate pi at each iteration
        out_file.write(f"{pi}\n")  # Save pi to the file

# Measure the end time
stop_time = time.time()
# Convert seconds to milliseconds
elapsed_time = (stop_time - start_time) * 1000

print("The values of pi have been written to 'pi_values.dat'.")
print(f"Execution time: {elapsed_time:.2f} milliseconds.")
