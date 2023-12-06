import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Load the model and scaler from the serialized files
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")


def categorize_track(features):
    # Scale the features using the loaded scaler
    scaled_features = scaler.transform([features])
    # Predict the category using the loaded model
    category = model.predict(scaled_features)
    return category
