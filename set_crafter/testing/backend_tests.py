```python
import unittest
from set_crafter.backend.spotify_auth import SpotifyAuth
from set_crafter.backend.track_downloader import TrackDownloader

class TestBackend(unittest.TestCase):

    def setUp(self):
        self.spotify_auth = SpotifyAuth()
        self.track_downloader = TrackDownloader()

    def test_spotify_auth(self):
        response = self.spotify_auth.authenticate()
        self.assertEqual(response.status_code, 200)

    def test_track_downloader(self):
        track_id = '6rqhFgbbKwnb9MLmUQDhG6'  # example track id
        track_data = self.track_downloader.download(track_id)
        self.assertIsNotNone(track_data)
        self.assertEqual(track_data['id'], track_id)

if __name__ == '__main__':
    unittest.main()
```