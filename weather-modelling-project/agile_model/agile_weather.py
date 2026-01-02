import numpy as np

def load_data():
    return np.loadtxt("../data/temperature_data.txt")

def train_model(days, temperature):
    return np.polyfit(days, temperature, 2)

def predict(days, coeffs):
    a, b, c = coeffs
    return a * days**2 + b * days + c

def display(days, actual, predicted):
    for i in range(len(days)):
        print(f"Day {i}: Actual={actual[i]}, Predicted={predicted[i]:.2f}")

temperature = load_data()
days = np.arange(len(temperature))

coeffs = train_model(days, temperature)
predicted = predict(days, coeffs)

print("Agile Weather Modelling Output\n")
display(days, temperature, predicted)
