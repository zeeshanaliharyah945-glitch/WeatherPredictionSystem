import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load model
model = joblib.load("../models/weather_model.pkl")
label_encoder = joblib.load("../models/label_encoder.pkl")

# Prediction function
def predict_weather():
    try:
        temp = float(temp_entry.get())
        humidity = float(humidity_entry.get())
        pressure = float(pressure_entry.get())
        wind = float(wind_entry.get())

        features = np.array([[temp, humidity, pressure, wind]])

        prediction = model.predict(features)

        weather = label_encoder.inverse_transform(prediction)

        result_label.config(text=f"Predicted Weather: {weather[0]}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

# GUI Window
root = tk.Tk()
root.title("Weather Prediction System")
root.geometry("400x400")

# Title
title = tk.Label(root, text="Weather Prediction System",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

# Temperature
tk.Label(root, text="Temperature").pack()
temp_entry = tk.Entry(root)
temp_entry.pack()

# Humidity
tk.Label(root, text="Humidity").pack()
humidity_entry = tk.Entry(root)
humidity_entry.pack()

# Pressure
tk.Label(root, text="Pressure").pack()
pressure_entry = tk.Entry(root)
pressure_entry.pack()

# Wind Speed
tk.Label(root, text="Wind Speed").pack()
wind_entry = tk.Entry(root)
wind_entry.pack()

# Predict Button
predict_btn = tk.Button(root, text="Predict Weather",
                        command=predict_weather,
                        bg="blue", fg="white")
predict_btn.pack(pady=20)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Run GUI
root.mainloop()