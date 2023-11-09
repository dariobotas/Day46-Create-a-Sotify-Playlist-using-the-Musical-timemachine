import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

if __name__ == '__main__':
  year_to_travel = input("Wich year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

  url_scrap = f"{URL}{year_to_travel}"
  response = requests.get(url_scrap).text
  soup = BeautifulSoup(response, "html.parser")
 
  """ Songs List """
  h3_songs = soup.select("li ul li h3")
  songs = [song.text.strip() for song in h3_songs]
  #print(songs)
  
  
  """ Artists List """
  span_artists = soup.select("li ul li:first-child span")
  artists = [artist.text.strip() for artist in span_artists]
  #print(artists)
  
  
  """ Print Songs / Artists List """
  for i in range(len(songs)):
    print(f"{i+1}. Song: {songs[i]} / Artist: {artists[i]}")