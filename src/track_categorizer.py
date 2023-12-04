from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from typing import List, Dict


class TrackCategorizer:
    def __init__(self):
        self.model = KNeighborsClassifier(n_neighbors=5)
        self.scaler = StandardScaler()

    def train_model(self, features: pd.DataFrame, target: pd.Series):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        # Scale the features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        # Train the KNN model
        self.model.fit(X_train_scaled, y_train)
        # Placeholder for model evaluation (e.g., accuracy score)

    def categorize_tracks(self, track_data: List[Dict[str, any]]) -> List[str]:
        # Convert track data to a DataFrame
        df = pd.DataFrame(track_data)
        # Select features for categorization
        features = df[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]
        # Scale the features
        features_scaled = self.scaler.transform(features)
        # Predict categories
        categories = self.model.predict(features_scaled)
        return categories.tolist()
