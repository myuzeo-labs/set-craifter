```python
import pandas as pd
from sklearn.model_selection import train_test_split

class ModelTrainingDataBuilder:
    def __init__(self, track_data):
        self.track_data = track_data

    def build_training_data(self):
        # Split the data into features and target
        X = self.track_data.drop('category', axis=1)
        y = self.track_data['category']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test
```