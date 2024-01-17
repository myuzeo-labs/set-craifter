```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from set_crafter.config import spotify_credentials

def authenticate_spotify():
    """Authenticate with Spotify using OAuth 2.0."""
    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=spotify_credentials['client_id'],
        client_secret=spotify_credentials['client_secret'],
        redirect_uri=spotify_credentials['redirect_uri'],
        scope=scope))

    return sp
```