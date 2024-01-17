```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import spotify_credentials

class SpotifyDataDownloader:
    def __init__(self):
        self.client_credentials_manager = SpotifyClientCredentials(client_id=spotify_credentials['client_id'], client_secret=spotify_credentials['client_secret'])
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def download_data(self, track_id):
        track_data = self.sp.track(track_id)
        return track_data
```