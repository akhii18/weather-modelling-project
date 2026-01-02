import numpy as np

temperature = np.loadtxt("../data/temperature_data.txt")
days = np.arange(len(temperature))

print("Iterative Weather Modelling\n")

for iteration in range(1, 4):
    t_subset = days[:iteration * 3]
    temp_subset = temperature[:iteration * 3]

    a, b, c = np.polyfit(t_subset, temp_subset, 2)

    print(f"Iteration {iteration}")
    print(f"T(t) = {a:.2f}t^2 + {b:.2f}t + {c:.2f}\n")
