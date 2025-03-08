import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 3:
    print("Usage: python plot.py <title> <path>")
    sys.exit(1)

title = sys.argv[1]
path = sys.argv[2]

# Read data from file
with open(path, 'r') as file:
    data = [float(line.strip()) for line in file]

# Calculate the average
average_value = sum(data) / len(data)

# Plotting the data
plt.plot(data, marker='o', linestyle='-')

# Adding title, labels, and average
plt.title(title)
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.axhline(y=average_value, color='r', linestyle='--',
            label=f'Average: {average_value:.2f}')

# Display the plot with a legend
	
