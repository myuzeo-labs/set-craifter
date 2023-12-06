import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyIntegration:
    def __init__(self, client_id, client_secret):
        client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        )
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_track_features(self, track_id):
        return self.sp.audio_features(track_id)[0]
