```python
import streamlit as st
from set_crafter.app.set_crafter_app import SetCrafterApp

def run_streamlit_app():
    st.title('SetCrafter AI')
    st.write('Welcome to SetCrafter AI, a tool designed to assist DJs in crafting their music sets with the help of AI-driven recommendations and data analysis.')

    spotify_credentials = st.text_input('Enter your Spotify credentials:')
    if spotify_credentials:
        app = SetCrafterApp(spotify_credentials)
        st.write('Spotify credentials set successfully.')

        if st.button('Start Categorizing and Curating'):
            try:
                app.run()
                st.write('Categorization and curation completed successfully.')
            except Exception as e:
                st.write(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    run_streamlit_app()
```