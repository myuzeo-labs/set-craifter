```python
import os
from set_crafter.data_preprocessing.dj_library_data_extractor import DJLibraryDataExtractor
from set_crafter.data_preprocessing.data_preprocessor import DataPreprocessor
from set_crafter.data_preprocessing.spotify_data_downloader import SpotifyDataDownloader
from set_crafter.ai_models.track_categorizer import TrackCategorizer
from set_crafter.ai_models.set_curator import SetCurator
from set_crafter.ai_models.model_training_data_builder import ModelTrainingDataBuilder

class SetCrafterApp:
    def __init__(self):
        self.spotify_credentials = os.getenv('SPOTIFY_CREDENTIALS')
        self.data_extractor = DJLibraryDataExtractor()
        self.data_preprocessor = DataPreprocessor()
        self.data_downloader = SpotifyDataDownloader(self.spotify_credentials)
        self.track_categorizer = TrackCategorizer()
        self.set_curator = SetCurator()
        self.training_data_builder = ModelTrainingDataBuilder()

    def run(self):
        # Extract data from DJ's library
        track_data = self.data_extractor.extract_data()

        # Download additional track data from Spotify
        track_data = self.data_downloader.download_data(track_data)

        # Preprocess the data for AI model consumption
        track_data = self.data_preprocessor.preprocess_data(track_data)

        # Build training data for AI models
        training_data = self.training_data_builder.build_training_data(track_data)

        # Categorize tracks based on their features
        categorized_tracks = self.track_categorizer.categorize_track(training_data)

        # Curate music sets based on the categorized tracks
        curated_sets = self.set_curator.curate_set(categorized_tracks)

        return curated_sets

if __name__ == "__main__":
    app = SetCrafterApp()
    curated_sets = app.run()
    print(curated_sets)
```