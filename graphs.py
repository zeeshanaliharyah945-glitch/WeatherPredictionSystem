import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/weather.csv")

plt.plot(data['temperature'])
plt.title("Temperature Graph")
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.show()