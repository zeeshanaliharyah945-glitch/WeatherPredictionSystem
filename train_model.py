import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib



# Load dataset
data = pd.read_csv("dataset/weather.csv")

# Remove null values
data = data.dropna()

# Encode target labels
le = LabelEncoder()
data['weather'] = le.fit_transform(data['weather'])

# Features and target
X = data[['temperature', 'humidity', 'pressure', 'wind_speed']]
y = data['weather']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/weather_model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("Model Saved Successfully!")