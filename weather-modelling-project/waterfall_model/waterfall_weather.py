import numpy as np

temperature = np.loadtxt("../data/temperature_data.txt")
days = np.arange(len(temperature))

coefficients = np.polyfit(days, temperature, 2)
a, b, c = coefficients

predicted = a * days**2 + b * days + c

print("Waterfall Model Weather Prediction")
print(f"T(t) = {a:.2f}t^2 + {b:.2f}t + {c:.2f}")

for i in range(len(days)):
    print(f"Day {i}: Actual={temperature[i]}, Predicted={predicted[i]:.2f}")
