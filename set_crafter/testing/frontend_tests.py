```python
import unittest
from unittest.mock import patch
from set_crafter.frontend.streamlit_app import SetCrafterApp

class TestFrontend(unittest.TestCase):

    @patch('streamlit.button')
    def test_spotify_auth_button(self, mock_button):
        mock_button.return_value = True
        app = SetCrafterApp()
        self.assertTrue(app.spotify_auth_button())

    @patch('streamlit.button')
    def test_track_download_button(self, mock_button):
        mock_button.return_value = True
        app = SetCrafterApp()
        self.assertTrue(app.track_download_button())

    @patch('streamlit.button')
    def test_data_preprocess_button(self, mock_button):
        mock_button.return_value = True
        app = SetCrafterApp()
        self.assertTrue(app.data_preprocess_button())

    @patch('streamlit.button')
    def test_track_categorize_button(self, mock_button):
        mock_button.return_value = True
        app = SetCrafterApp()
        self.assertTrue(app.track_categorize_button())

    @patch('streamlit.button')
    def test_set_curate_button(self, mock_button):
        mock_button.return_value = True
        app = SetCrafterApp()
        self.assertTrue(app.set_curate_button())

if __name__ == '__main__':
    unittest.main()
```