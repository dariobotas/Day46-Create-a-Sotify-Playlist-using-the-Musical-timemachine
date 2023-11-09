import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

if __name__ == '__main__':
  year_to_travel = input("Wich year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

  url_scrap = f"{URL}{year_to_travel}"

  response = requests.get(url_scrap).text
 
  soup = BeautifulSoup(response, "html.parser")
 
  """ Songs List """
  h3_songs = soup.find_all('h3', id="title-of-a-story", 
                           class_=("a-no-trucate",
                                   "lrv-u-font-size-16", 
                                   "u-line-height-125", 
                                   "u-line-height-normal@mobile-max a-truncate-ellipsis"
                                  ))
  print(len(h3_songs))
  
  tag_songs = [song for song in h3_songs if len(song) != 0]
  songs = [str(song.text).strip("\n\t") 
           for songs in tag_songs 
           for song in songs
          ]
  
  
  """ Artists List """
  span_artists = soup.find_all('span', class_=("a-no-trucate",
                                               "lrv-u-font-size-14@mobile-max","u-line-height-normal@mobile-max",
                                               "u-letter-spacing-0021",
                                               
                                               "a-truncate-ellipsis-2line",
                                               "u-max-width-330","u-max-width-230@tablet-only"))
  tag_artists = [artist for artist in span_artists if len(artist) != 0]
  artists = [
    str(artist.text).strip("\n\t") 
    for artists in tag_artists 
    for artist in artists
  ]
  print(len(artists))

  """ Print Songs / Artists List """
  for i in range(len(artists)):
    print(f"{i+1}. Song: {songs[i]} / Artist: {artists[i]}")