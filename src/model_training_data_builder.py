import pandas as pd
from typing import List


class ModelTrainingDataBuilder:
    def __init__(self):
        self.data = pd.DataFrame()

    def add_track_features(self, track_features: dict):
        self.data = self.data.append(track_features, ignore_index=True)

    def prepare_dataset(
        self, track_ids: List[str], spotify_integration: "SpotifyIntegration"
    ):
        for track_id in track_ids:
            features = spotify_integration.get_track_features(track_id)
            self.add_track_features(features)
        return self.data
