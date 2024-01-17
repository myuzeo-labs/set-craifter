```python
import streamlit as st
from set_crafter.app.set_crafter_app import SetCrafterApp

def main():
    st.title("SetCrafter AI")
    st.write("Welcome to SetCrafter AI, a tool designed to assist DJs in crafting their music sets with the help of AI-driven recommendations and data analysis.")

    spotify_auth_button = st.button("Authenticate with Spotify")
    if spotify_auth_button:
        SetCrafterApp.authenticate_spotify()

    track_download_button = st.button("Download Track Data")
    if track_download_button:
        SetCrafterApp.download_data()

    data_preprocess_button = st.button("Preprocess Data")
    if data_preprocess_button:
        SetCrafterApp.preprocess_data()

    track_categorize_button = st.button("Categorize Tracks")
    if track_categorize_button:
        SetCrafterApp.categorize_track()

    set_curate_button = st.button("Curate Set")
    if set_curate_button:
        SetCrafterApp.curate_set()

if __name__ == "__main__":
    main()
```