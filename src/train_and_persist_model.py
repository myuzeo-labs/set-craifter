import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Simulated dataset
# Features: danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo
# Target: category

# Generate a simulated dataset
data = {
    'danceability': [0.7, 0.8],
    'energy': [0.6, 0.9],
    'key': [5, 8],
    'loudness': [-5, -3],
    'mode': [1, 0],
    'speechiness': [0.05, 0.04],
    'acousticness': [0.1, 0.3],
    'instrumentalness': [0.0, 0.2],
    'liveness': [0.1, 0.2],
    'valence': [0.6, 0.8],
    'tempo': [120, 130],
    'category': ['buildup', 'mainstage']
}
df = pd.DataFrame(data)

# Split the data into features and target
X = df.drop('category', axis=1)
y = df['category']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the KNN model
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train_scaled, y_train)

# Evaluate the model using accuracy score
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy:.2f}')

# Save the model and scaler to disk
joblib.dump(model, 'model.joblib')
joblib.dump(scaler, 'scaler.joblib')
