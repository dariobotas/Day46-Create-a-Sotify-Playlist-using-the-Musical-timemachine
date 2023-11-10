import os

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIFY_REDIRECT_URI"]
URL = "https://www.billboard.com/charts/hot-100/"

if __name__ == '__main__':
  """ Step 1"""
  year_to_travel = input("Wich year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

  url_scrap = f"{URL}{year_to_travel}"
  response = requests.get(url_scrap).text
  soup = BeautifulSoup(response, "html.parser")
 
  """ Songs List scraping on Billboard """
  h3_songs = soup.select("li ul li h3")
  songs = [song.text.strip() for song in h3_songs]
  #print(songs)

  """ Step 2 """
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

  results = spotify.current_user()["id"]
  print(results)

  """ Step 3 """
  #Searching Spotify for songs by title
  song_uris = []
  year = year_to_travel.split("-")[0]
  for song in songs:
      result = spotify.search(q=f"track:{song} year:{year}", type="track")
      print(result)
      try:
          uri = result["tracks"]["items"][0]["uri"]
          song_uris.append(uri)
      except IndexError:
          print(f"{song} doesn't exist in Spotify. Skipped.")

  """ Step 4 """
  #Creating a new private playlist in Spotify
  playlist = spotify.user_playlist_create(user=results, name=f"{year_to_travel} Billboard 100", public=False)
  print(playlist)

  #Adding songs found into the new playlist
  spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
  print(len(song_uris))