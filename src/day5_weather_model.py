import os
import time

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

from weather_api import get_weather


INPUT_FILE = "processed/road_conditions_cleaned.csv"


# ---------------------------------------------------------
# Demo State -> City mapping
# 5 states with positive 2014 pothole target
# 5 states with zero 2014 pothole target
# ---------------------------------------------------------

state_city = {
    "Madhya Pradesh": "Bhopal",
    "Uttar Pradesh": "Lucknow",
    "Tamil Nadu": "Chennai",
    "Maharashtra": "Mumbai",
    "Gujarat": "Ahmedabad",
    "Haryana": "Gurugram",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Sikkim": "Gangtok",
}


# ---------------------------------------------------------
# Load cleaned MoRTH dataset
# ---------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

# Remove national Total row
df = df[df["state_ut"] != "Total"].copy()


# ---------------------------------------------------------
# Create target
# ---------------------------------------------------------

df["risk_target"] = (
    df["rutted_pot_holes_accident_2014"] > 0
).astype(int)


# ---------------------------------------------------------
# Select the 10-state demo subset
# ---------------------------------------------------------

df = df[df["state_ut"].isin(state_city.keys())].copy()

print("Selected states:", len(df))


# ---------------------------------------------------------
# Fetch weather for each demo city
# ---------------------------------------------------------

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    raise ValueError("OPENWEATHER_API_KEY is not set")


weather_rows = []

for state, city in state_city.items():
    print(f"Fetching weather for {state} -> {city}")

    weather = get_weather(city, api_key)

    weather_rows.append({
        "state_ut": state,
        "temperature": weather["temperature"],
        "humidity": weather["humidity"],
        "weather_condition": weather["condition"],
        "weather_timestamp": weather["timestamp"],
    })

    # Small delay between API calls
    time.sleep(1)


weather_df = pd.DataFrame(weather_rows)


# ---------------------------------------------------------
# Merge MoRTH + weather
# ---------------------------------------------------------

df = df.merge(
    weather_df,
    on="state_ut",
    how="inner"
)


# ---------------------------------------------------------
# Model features
# ---------------------------------------------------------

road_features = [
    "speed_breakers_number_of_accidents_2016",
    "sharp_curve_number_of_accidents_2016",
    "steep_gradient_number_of_accidents_2016",
]

weather_features = [
    "temperature",
    "humidity",
]

features = road_features + weather_features

X = df[features].fillna(0)
y = df["risk_target"]


# ---------------------------------------------------------
# Train/test split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# ---------------------------------------------------------
# Scale numerical features + Logistic Regression
# ---------------------------------------------------------

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# ---------------------------------------------------------
# Evaluation
# ---------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


print("\nDay 5 Weather-Integrated Model")
print("--------------------------------")

print("Features:")
for feature in features:
    print("-", feature)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nAccuracy:", round(accuracy, 4))
print("F1 Score:", round(f1, 4))

print("\nWeather data used:")
print(
    df[
        [
            "state_ut",
            "temperature",
            "humidity",
            "weather_condition",
        ]
    ].to_string(index=False)
)