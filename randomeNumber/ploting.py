def calculate_e(approx_iterations):
    approx_e = (1 + 1 / approx_iterations) ** approx_iterations
    return approx_e


# Example: Calculate "e" with 1000000 iterations
approximation_iterations = 1000000
approx_e_value = calculate_e(approximation_iterations)

print(
    f"Approximation of e with {approximation_iterations} iterations: {approx_e_value}")
