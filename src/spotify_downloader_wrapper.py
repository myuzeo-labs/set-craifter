import subprocess
import os


class SpotifyDownloaderWrapper:
    def __init__(self, download_directory: str = "downloads"):
        self.download_directory = download_directory
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)

    def download_track(self, track_uri: str):
        subprocess.run(
            ["spotdl", track_uri, "--output", self.download_directory], check=True
        )

    def download_playlist(self, playlist_uri: str):
        subprocess.run(
            ["spotdl", playlist_uri, "--output", self.download_directory], check=True
        )

    def download_album(self, album_uri: str):
        subprocess.run(
            ["spotdl", album_uri, "--output", self.download_directory], check=True
        )
