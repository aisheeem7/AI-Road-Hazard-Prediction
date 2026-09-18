import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


INPUT_FILE = "processed/road_conditions_cleaned.csv"


# ---------------------------------------------------------
# Load cleaned dataset
# ---------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

# Remove national Total row
df = df[df["state_ut"] != "Total"].copy()


# ---------------------------------------------------------
# Create target
# 1 = reported pothole accidents in 2014
# 0 = no reported pothole accidents in 2014
# ---------------------------------------------------------

df["risk_target"] = (
    df["rutted_pot_holes_accident_2014"] > 0
).astype(int)


# ---------------------------------------------------------
# Day 4 leakage-reduced feature set
#
# We intentionally exclude:
# - 2014 pothole deaths
# - 2014 pothole injuries
# - 2016 pothole accident/death/injury fields
#
# These are either direct outcomes related to the target
# or occur after the 2014 target year.
# ---------------------------------------------------------

features = [
    "speed_breakers_number_of_accidents_2016",
    "sharp_curve_number_of_accidents_2016",
    "steep_gradient_number_of_accidents_2016",
]


X = df[features].fillna(0)
y = df["risk_target"]


# ---------------------------------------------------------
# Train/test split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# ---------------------------------------------------------
# Logistic Regression
# ---------------------------------------------------------

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# ---------------------------------------------------------
# Evaluation
# ---------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


print("Day 4 Leakage-Reduced Model")
print("--------------------------------")
print("Features:")
for feature in features:
    print("-", feature)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nAccuracy:", round(accuracy, 4))
print("F1 Score:", round(f1, 4))