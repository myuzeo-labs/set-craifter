```python
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

class TrackCategorizer:
    def __init__(self):
        self.model = KNeighborsClassifier()

    def build_training_data(self, track_data):
        # Extract features and labels from track_data
        features = track_data.drop('category', axis=1)
        labels = track_data['category']
        return features, labels

    def train_model(self, features, labels):
        self.model.fit(features, labels)

    def categorize_track(self, track):
        # Predict the category of a single track
        category = self.model.predict([track])
        return category[0]

if __name__ == "__main__":
    track_data = pd.read_csv('track_data.csv')
    categorizer = TrackCategorizer()
    features, labels = categorizer.build_training_data(track_data)
    categorizer.train_model(features, labels)
    test_track = [0.6, 0.7, 120]  # Example track data
    print(categorizer.categorize_track(test_track))
```