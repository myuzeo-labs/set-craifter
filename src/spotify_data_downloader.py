import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import List, Dict


class SpotifyDataDownloader:
    def __init__(self, client_id: str, client_secret: str):
        credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=credentials_manager)

    def download_track_data(self, track_ids: List[str]) -> List[Dict[str, any]]:
        track_data = []
        for track_id in track_ids:
            try:
                track_info = self.sp.track(track_id)
                track_features = self.sp.audio_features(track_id)[0]
                track_data.append({**track_info, **track_features})
            except spotipy.exceptions.SpotifyException as e:
                raise Exception(f'Failed to download data for track ID {track_id}: {e}')
        return track_data
