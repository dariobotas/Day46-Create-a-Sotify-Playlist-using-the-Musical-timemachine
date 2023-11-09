import requests
from bs4 import BeautifulSoup

#from selenium import webdriver

URL = "https://www.billboard.com/charts/hot-100/"

if __name__ == '__main__':
  #year_to_travel = input("Wich year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

  url_scrap = f"{URL}2000-08-12"  #{year_to_travel}"
  #print(url_scrap)

  #driver = webdriver.Edge()
  #driver.get(url_scrap)
  response = requests.get(url_scrap).text
  #soup = BeautifulSoup(driver.page_source, "html.parser")
  soup = BeautifulSoup(response, "html.parser")
  #print(soup.body.contents)
  #driver.quit()
  #title_and_song_li_tags = soup.find_all("li", class_="lrv-u-width-100p")
  #uls = list(title_and_song_li_tags)
  """ Songs List """
  h3_songs = soup.find_all('h3', id="title-of-a-story", 
                           class_=("a-no-trucate",
                                   "lrv-u-font-size-16", 
                                   "u-line-height-125", 
                                   "u-line-height-normal@mobile-max a-truncate-ellipsis"
                                  ))
  print(len(h3_songs))
  #print(h3_songs[::2])
  tag_songs = [song for song in h3_songs if len(song) != 0]
  songs = [str(song.text).strip("\n\t") for songs in tag_songs for song in songs]
  #print(songs)
  #songs = []
  #for song in tag_songs:
  #  for i in song:
  #    song = i.text
  #    songs.append(str(song).strip("\n\t"))
  #print(songs)
  
  """ Artists List """
  span_artists = soup.find_all('span', class_=("a-no-trucate",
                                               "lrv-u-font-size-14@mobile-max","u-line-height-normal@mobile-max",
                                               "u-letter-spacing-0021",
                                               
                                               "a-truncate-ellipsis-2line",
                                               "u-max-width-330","u-max-width-230@tablet-only"))
  tag_artists = [artist for artist in span_artists if len(artist) != 0]
  artists = [
    str(artist.text).strip("\n\t") for artists in tag_artists 
    for artist in artists
  ]
  print(len(artists))
  print(artists)
  #print(f"Songs: {len(h3_songs[::2])}- Artists: {len(span_artists[::2])}")
  #print(f"Songs: {len(songs)}- Artists: {len(artists)}")
  #print([f"Song/Artist: {songs[i]} - {artists[i]}" for i in range(len(songs))])
  #titles_and_songs = [title for title in uls_inside_lis]
  #rest=[title.find_all("h3") for title in titles_and_songs]
  #print(rest[0].getText())
  #titles = soup.find_all("h3", id="title-of-a-story", class_="c-title")f"Title/Artist: {title.find_all("h3").getText()} - {title.find_all("span").getText()}"
  #print([title.getText().replace("\n", "").replace("\t","") for title in titles])

  #body_content = soup.body.contents
  #with open("billboard.txt", mode="w") as file:
  #    for line in body_content:
  #        file.write(f"{line}\n")
  #print(soup.prettify())
