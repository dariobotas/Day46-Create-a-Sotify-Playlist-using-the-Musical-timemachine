import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIFY_REDIRECT_URI"]

def run():
  spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
      client_id=SPOTIFY_CLIENT_ID,
      client_secret=SPOTIFY_CLIENT_SECRET,
      redirect_uri="http://example.com",
      scope="playlist-modify-private",
      show_dialog=True,
      cache_path="token.txt",
      username="21c2udkjgxynwcj6re46edsny" 
    ))
  
  results = spotify.current_user()
  print(results)
  user_id = results["id"]
  print(f"User is: {user_id}")