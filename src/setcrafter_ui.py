import streamlit as st
from dj_library_data_extractor import DJLibraryDataExtractor
from data_preprocessor import DataPreprocessor
from spotify_data_downloader import SpotifyDataDownloader
from track_categorizer import TrackCategorizer
from set_curator import SetCurator
from spotify_integration import SpotifyIntegration


def main():
    st.title('SetCrafter AI')

    st.header('Welcome to SetCrafter AI')
    st.write('This tool assists DJs in organizing and curating their music libraries with the help of AI.')

    if st.button('Start Categorizing'):
        st.write('Categorization process will start.')
        # Instantiate the necessary classes
        extractor = DJLibraryDataExtractor()
        preprocessor = DataPreprocessor()
        # TODO: Replace with actual Spotify credentials
        downloader = SpotifyDataDownloader(client_id='your_client_id', client_secret='your_client_secret')
        categorizer = TrackCategorizer()

        # Example steps for the categorization process
        library_path = st.text_input('Enter your music library path:')
        if library_path:
            raw_data = extractor.extract_data(library_path)
            preprocessed_data = preprocessor.process_data(raw_data)
            track_ids = [track['id'] for track in preprocessed_data]
            track_data = downloader.download_track_data(track_ids)
            categorized_tracks = categorizer.categorize_tracks(track_data)
            st.write('Categorization complete!')

    if st.button('Curate Set'):
        st.write('Set curation process will start.')
        curator = SetCurator()
        # Example steps for the set curation process
        categorized_tracks = []  # Placeholder for categorized tracks
        curated_set = curator.curate_set(categorized_tracks)
        st.write('Set curation complete!')

if __name__ == '__main__':
    main()
