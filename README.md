# Weather Prediction System

A machine learning based Weather Prediction System developed in Python. The project uses a Random Forest Classifier to predict weather conditions from temperature, humidity, pressure, and wind speed. It also includes a Tkinter GUI for entering weather data and displaying the predicted weather condition.

## Features

- Weather prediction using Machine Learning
- Random Forest Classifier
- Predicts weather from:
  - Temperature
  - Humidity
  - Pressure
  - Wind Speed
- Simple Tkinter desktop GUI
- Dataset visualization using Matplotlib
- Saved trained model and label encoder
- Easy model retraining using the included dataset

## Project Structure

```text
WeatherPredictionSystem/
│
├── dataset/
│   └── weather.csv
│
├── gui/
│   └── app.py
│
├── models/
│   ├── label_encoder.pkl
│   └── weather_model.pkl
│
├── graphs.py
├── train_model.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Tkinter

## Machine Learning Model

The project uses a `RandomForestClassifier` from Scikit-learn.

### Input Features

- `temperature`
- `humidity`
- `pressure`
- `wind_speed`

### Target

- `weather`

The weather labels are converted into numeric values using `LabelEncoder`.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd WeatherPredictionSystem
```

Or download the repository as a ZIP file and extract it.

### 2. Install required packages

```bash
pip install -r requirements.txt
```

> Tkinter is included with most standard Python installations on Windows and is not installed through `pip`.

## How to Run

### Run the trained Weather Prediction GUI

From the project folder:

```bash
cd gui
python app.py
```

Enter temperature, humidity, pressure, and wind speed, then click **Predict Weather**.

### Retrain the Machine Learning Model

Run this command from the main project folder:

```bash
python train_model.py
```

The script will:

1. Load `dataset/weather.csv`
2. Remove missing values
3. Encode weather labels
4. Split the dataset into training and testing data
5. Train a Random Forest model
6. Display model accuracy
7. Save the trained model in the `models` folder

### Display the Temperature Graph

Run from the main project folder:

```bash
python graphs.py
```

## Dataset

The dataset is stored at:

```text
dataset/weather.csv
```

The model uses the following columns:

```text
temperature
humidity
pressure
wind_speed
weather
```

## Model Files

The trained model files are stored in:

```text
models/weather_model.pkl
models/label_encoder.pkl
```

## Purpose

This project demonstrates how machine learning can be used to predict weather conditions from common weather measurements while providing a simple graphical interface for users.

## Author

Developed as a Computer Science / Machine Learning project.
