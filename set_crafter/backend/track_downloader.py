```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ..config import spotify_credentials

class SpotifyDataDownloader:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_credentials['client_id'],
                                                            client_secret=spotify_credentials['client_secret'],
                                                            redirect_uri=spotify_credentials['redirect_uri'],
                                                            scope=spotify_credentials['scope']))

    def download_data(self, track_id):
        track_data = self.sp.track(track_id)
        return track_data
```