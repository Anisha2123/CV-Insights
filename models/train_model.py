

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load labeled resumes
df = pd.read_csv("../data/labeled_resumes.csv")

X = df.drop(columns=["ATS_Score"])  # Features (resume text, keywords)
y = df["ATS_Score"]  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "../models/ats_model.pkl")  # Save model
print("✅ Model trained and saved as ats_model.pkl!")
