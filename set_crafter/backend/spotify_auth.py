```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, redirect, session
import os
from ..config import spotify_credentials

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session["token_info"] = token_info
    return redirect("AuthenticationSuccess")

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=spotify_credentials["client_id"],
        client_secret=spotify_credentials["client_secret"],
        redirect_uri=spotify_credentials["redirect_uri"],
        scope="user-library-read"
    )

def get_token(session):
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token.
    if not (session.get('token_info', False)):
        token_valid = False
    else:
        now = int(time.time())
        is_token_expired = session['token_info']['expires_at'] - now < 60

        # If the token is expired, refresh it
        if (is_token_expired):
            sp_oauth = create_spotify_oauth()
            token_info = sp_oauth.refresh_access_token(session['token_info']['refresh_token'])
        token_valid = True
    return token_info, token_valid

if __name__ == "__main__":
    app.run(debug=True, port=spotify_credentials["port"])
```