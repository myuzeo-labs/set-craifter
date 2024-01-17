Shared Dependencies:

1. **Variables:**
   - `spotify_credentials`: Spotify API credentials used in `config.py`, `spotify_auth.py`, and `spotify_data_downloader.py`.
   - `track_data`: Data extracted from DJ's library, used in `dj_library_data_extractor.py`, `data_preprocessor.py`, `track_categorizer.py`, and `set_curator.py`.

2. **Data Schemas:**
   - `TrackSchema`: Schema for track data, used in `dj_library_data_extractor.py`, `data_preprocessor.py`, `track_categorizer.py`, and `set_curator.py`.
   - `SetSchema`: Schema for curated sets, used in `set_curator.py` and `set_crafter_app.py`.

3. **Function Names:**
   - `extract_data()`: Function in `dj_library_data_extractor.py`, used in `set_crafter_app.py`.
   - `preprocess_data()`: Function in `data_preprocessor.py`, used in `set_crafter_app.py`.
   - `download_data()`: Function in `spotify_data_downloader.py`, used in `set_crafter_app.py`.
   - `categorize_track()`: Function in `track_categorizer.py`, used in `set_crafter_app.py`.
   - `curate_set()`: Function in `set_curator.py`, used in `set_crafter_app.py`.
   - `build_training_data()`: Function in `model_training_data_builder.py`, used in `track_categorizer.py` and `set_curator.py`.

4. **Message Names:**
   - `AuthenticationSuccess`: Message sent from `spotify_auth.py` to `set_crafter_app.py` upon successful Spotify authentication.
   - `DataDownloaded`: Message sent from `spotify_data_downloader.py` to `set_crafter_app.py` upon successful data download.
   - `DataPreprocessed`: Message sent from `data_preprocessor.py` to `set_crafter_app.py` upon successful data preprocessing.
   - `TrackCategorized`: Message sent from `track_categorizer.py` to `set_crafter_app.py` upon successful track categorization.
   - `SetCurated`: Message sent from `set_curator.py` to `set_crafter_app.py` upon successful set curation.

5. **DOM Element IDs:**
   - `spotify-auth-button`: Button for Spotify authentication in `streamlit_app.py`.
   - `track-download-button`: Button for track downloading in `streamlit_app.py`.
   - `data-preprocess-button`: Button for data preprocessing in `streamlit_app.py`.
   - `track-categorize-button`: Button for track categorization in `streamlit_app.py`.
   - `set-curate-button`: Button for set curation in `streamlit_app.py`.

6. **Libraries:**
   - `spotipy`: Used in `spotify_auth.py` and `spotify_data_downloader.py`.
   - `pandas`: Used in `dj_library_data_extractor.py`, `data_preprocessor.py`, `track_categorizer.py`, and `set_curator.py`.
   - `scikit-learn`: Used in `track_categorizer.py` and `set_curator.py`.
   - `flask`: Used in `spotify_auth.py` and `flask_deployment.py`.
   - `streamlit`: Used in `streamlit_app.py` and `streamlit_deployment.py`.