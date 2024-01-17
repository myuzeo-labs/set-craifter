```python
import os
from set_crafter.config import spotify_credentials
from set_crafter.data_preprocessing.dj_library_data_extractor import DJLibraryDataExtractor
from set_crafter.data_preprocessing.data_preprocessor import DataPreprocessor
from set_crafter.data_preprocessing.spotify_data_downloader import SpotifyDataDownloader
from set_crafter.ai_models.track_categorizer import TrackCategorizer
from set_crafter.ai_models.set_curator import SetCurator
from set_crafter.ai_models.model_training_data_builder import ModelTrainingDataBuilder
from set_crafter.app.set_crafter_app import SetCrafterApp

def main():
    # Initialize modules
    data_extractor = DJLibraryDataExtractor()
    data_preprocessor = DataPreprocessor()
    data_downloader = SpotifyDataDownloader(spotify_credentials)
    track_categorizer = TrackCategorizer()
    set_curator = SetCurator()
    training_data_builder = ModelTrainingDataBuilder()

    # Initialize main application
    set_crafter_app = SetCrafterApp(data_extractor, data_preprocessor, data_downloader, track_categorizer, set_curator, training_data_builder)

    # Run the application
    set_crafter_app.run()

if __name__ == "__main__":
    main()
```