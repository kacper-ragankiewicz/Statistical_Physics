import numpy as np

Xn = np.random.randn(100)  # generate 100 random numbers for Xn

Xn_squared = Xn**2
Xn_mean = np.mean(Xn)
Xn_squared_mean = np.mean(Xn_squared)

V_Xn = Xn_squared_mean - Xn_mean**2

print(V_Xn)
