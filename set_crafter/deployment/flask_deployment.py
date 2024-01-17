```python
from flask import Flask
from set_crafter.backend.spotify_auth import SpotifyAuth
from set_crafter.backend.track_downloader import TrackDownloader

app = Flask(__name__)

spotify_auth = SpotifyAuth()
track_downloader = TrackDownloader()

@app.route('/spotify-auth', methods=['GET'])
def authenticate_spotify():
    return spotify_auth.authenticate()

@app.route('/download-track', methods=['POST'])
def download_track():
    return track_downloader.download()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```