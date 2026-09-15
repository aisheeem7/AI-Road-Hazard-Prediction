import pandas as pd
import os

# Raw MoRTH CSV is intentionally not committed to GitHub.
# Obtain it from the official data.gov.in/MoRTH resource and place it at:
# data/raw/Acc_clf_acco_to_Road_Cond_2014_and_2016.csv

INPUT_FILE = "data/raw/Acc_clf_acco_to_Road_Cond_2014_and_2016.csv"
OUTPUT_FILE = "processed/road_conditions_cleaned.csv"

# Load raw dataset
df = pd.read_csv(INPUT_FILE)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace("/", "_", regex=False)
    .str.replace("-", "_", regex=False)
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace(" ", "_", regex=False)
)

# Convert S. No. to nullable integer
df["s_no"] = pd.to_numeric(df["s_no"], errors="coerce").astype("Int64")

# Convert all other non-state columns to numeric
for column in df.columns:
    if column != "state_ut" and column != "s_no":
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Keep the Total row as an aggregate row
# Its s_no is intentionally missing.
df.loc[df["state_ut"] == "Total", "s_no"] = pd.NA

# Create output directory
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Save cleaned dataset separately
df.to_csv(OUTPUT_FILE, index=False)

# Validation
print("Cleaned dataset saved to:", OUTPUT_FILE)
print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
